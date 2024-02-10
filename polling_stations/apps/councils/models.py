import re
from pathlib import Path

from data_importers.event_types import DataEventType
from django.apps import apps
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.db import DEFAULT_DB_ALIAS
from django.db.models import Count, JSONField, OuterRef, Subquery
from django.utils.translation import get_language
from file_uploads.models import File, Upload

from polling_stations.i18n.cy import WelshNameMutationMixin


class CouncilQueryset(models.QuerySet):
    def with_polling_stations_in_db(self):
        return (
            self.using(DEFAULT_DB_ALIAS)
            .annotate(ps_count=Count("pollingstation"))
            .exclude(pollingstation=None)
        )

    def with_ems_from_uploads(self):
        latest_ems_subquery = (
            File.objects.filter(upload=OuterRef("pk")).values("ems").distinct("ems")
        )
        upload_subquery = (
            Upload.objects.filter(gss=OuterRef("council_id"))
            .annotate(ems=latest_ems_subquery)
            .order_by("-timestamp")
        )

        return self.using(DEFAULT_DB_ALIAS).annotate(
            latest_ems=Subquery(upload_subquery.values("ems")[:1]),
            latest_upload_id=(upload_subquery.values("id")[:1]),
        )


class Council(WelshNameMutationMixin, models.Model):
    council_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(blank=True, max_length=255)
    name_translated = JSONField(default=dict)
    identifiers = ArrayField(models.CharField(max_length=100), default=list)

    electoral_services_email = models.EmailField(blank=True)
    electoral_services_phone_numbers = ArrayField(
        models.CharField(max_length=100), default=list
    )
    electoral_services_website = models.URLField(blank=True)
    electoral_services_postcode = models.CharField(
        blank=True, null=True, max_length=100
    )
    electoral_services_address = models.TextField(blank=True, null=True)

    registration_email = models.EmailField(blank=True)
    registration_phone_numbers = ArrayField(
        models.CharField(blank=True, max_length=100), default=list
    )
    registration_website = models.URLField(blank=True)
    registration_postcode = models.CharField(blank=True, null=True, max_length=100)
    registration_address = models.TextField(blank=True, null=True)

    users = models.ManyToManyField(through="UserCouncils", to=settings.AUTH_USER_MODEL)

    objects = CouncilQueryset.as_manager()

    def __str__(self):
        try:
            return self.name_translated[get_language()]
        except KeyError:
            return self.name

    class Meta:
        ordering = ("name",)

    @property
    def nation(self):
        nations_lookup = {
            "E": "England",
            "W": "Wales",
            "S": "Scotland",
            "N": "Northern Ireland",
        }
        # A GSS code is:
        #   'ANN' + 'NNNNNN' where 'A' is one of 'ENSW' and 'N' is 0-9.
        #   'ANN' section is the Entity Code.
        # We want to look for identifiers that look like GSS codes
        # for the types of organisations that manage elections.

        # Ref: https://geoportal.statistics.gov.uk/search?collection=Dataset&sort=-created&tags=all(PRD_RGC)
        gss_pattern = re.compile(
            """
            ^        # Start of string
            (        # Entity Codes:
                E06   # Unitary Authorities (England)
              | E07   # Non-metropolitan Districts (England)
              | E08   # Metropolitan Districts (England)
              | E09   # London Boroughs (England)
              | N09   # Local Government Districts (Northern Ireland)
              | S12   # Council Areas (Scotland)
              | W06   # Unitary Authorities (Wales)
            )
            [0-9]{6} # id
            $        # End of string
            """,
            re.VERBOSE,
        )
        identifier_matches = [
            identifier
            for identifier in self.identifiers
            if re.match(gss_pattern, identifier)
        ]
        identifier_nations = {
            nations_lookup[identifier[0]]
            for identifier in identifier_matches
            if identifier
        }
        if len(identifier_nations) == 1:
            return identifier_nations.pop()
        return ""

    @property
    def short_name(self):
        short_name = self.name
        extras = [
            "London Borough of ",
            "Royal Borough of ",
            "Council of the " "City of ",
            "City & County of ",
            " City & District Council",
            " City Council",
            " District Council",
            " Metropolitan",
            " Borough",
            " County",
            " Council",
        ]
        for extra in extras:
            short_name = short_name.replace(extra, "")
        return short_name

    @property
    def import_script_path(self):
        import_script_path = None

        scripts = Path(
            "./polling_stations/apps/data_importers/management/commands/"
        ).glob("import_*.py")
        for script in scripts:
            if f'council_id = "{self.council_id}"' in script.read_text():
                import_script_path = script
        if not import_script_path:
            import_script_path = Path(
                f'./polling_stations/apps/data_importers/management/commands/import_{self.short_name.lower().replace(" ", "_")}.py'
            )

        return str(import_script_path)

    @property
    def has_polling_stations_in_db(self):
        if self.pollingstation_set.count() > 0:
            return True
        return False

    def latest_data_event(self, event_type):
        data_event_model = apps.get_model("data_importers", "DataEvent")
        try:
            return self.dataevent_set.filter(event_type=event_type).latest()
        except data_event_model.DoesNotExist:
            return None

    @property
    def live_upload(self):
        if not self.has_polling_stations_in_db:
            return None
        latest_import = self.latest_data_event(DataEventType.IMPORT)
        latest_teardown = self.latest_data_event(DataEventType.TEARDOWN)
        if (
            latest_teardown
            and latest_import
            and (latest_import.created > latest_teardown.created)
            and latest_import.upload
        ):
            return latest_import.upload
        if latest_import and not latest_teardown and latest_import.upload:
            return latest_import.upload
        return None


class CouncilGeography(models.Model):
    council = models.OneToOneField(
        "Council", related_name="geography", on_delete=models.CASCADE
    )
    gss = models.CharField(blank=True, max_length=20)
    geography = models.MultiPolygonField(null=True)


class UserCouncils(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    council = models.ForeignKey(Council, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "User Councils"
