from addressbase.models import Address, UprnToCouncil
from data_importers.management.commands import BaseHalaroseCsvImporter
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseHalaroseCsvImporter):
    council_id = "EDN"
    addresses_name = "2024-05-02/2024-04-04T12:10:32.315869/Eros_SQL_Output003.csv"
    stations_name = "2024-05-02/2024-04-04T12:10:32.315869/Eros_SQL_Output003.csv"
    elections = ["2024-05-02"]

    def pre_import(self):
        # We need to consider rows that don't have a uprn when importing data.
        # However there are lots of rows for other councils in this file.
        # So build a list of stations from rows that do have UPRNS
        # and then use that list of stations to make sure we check relevant rows, even if they don't have a UPRN

        council_uprns = set(
            UprnToCouncil.objects.filter(lad=self.council.geography.gss).values_list(
                "uprn", flat=True
            )
        )
        self.COUNCIL_STATIONS = set()
        data = self.get_addresses()

        for record in data:
            if record.uprn in council_uprns:
                self.COUNCIL_STATIONS.add(record.pollingstationnumber)

    def address_record_to_dict(self, record):
        if record.pollingstationnumber not in self.COUNCIL_STATIONS:
            return None

        if record.housepostcode in [
            # split
            "CA4 0HR",
            "CA11 9HZ",
            "CA11 8BX",
            "CA9 3ND",
            "CA10 2DQ",
            "CA11 7UR",
        ]:
            return None
        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        if record.pollingstationnumber not in self.COUNCIL_STATIONS:
            return None
        return super().station_record_to_dict(record)

    # quick fix to show maps for Halarose records that have a valid UPRN in the PollingVenueUPRN field
    def get_station_point(self, record):
        uprn = record.pollingvenueuprn.strip().lstrip("0")
        try:
            ab_rec = Address.objects.get(uprn=uprn)
            return ab_rec.location
        except ObjectDoesNotExist:
            return super().get_station_point(record)
