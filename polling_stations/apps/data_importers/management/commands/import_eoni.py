import csv
from pathlib import Path

from django.contrib.gis.geos import Point
from django.db import connection

from addressbase.models import UprnToCouncil, Address
from polling_stations.settings.constants.councils import NIR_IDS
from councils.models import Council
from data_importers.base_importers import BaseStationsImporter, CsvMixin
from data_importers.data_types import StationSet
from pollingstations.models import PollingStation, CustomFinder

ADDRESSES_FIELDS = ["uprn", "address", "postcode", "location", "addressbase_postal"]
UPRN_FIELDS = ["uprn", "lad", "polling_station_id", "advance_voting_station_id"]
STATION_FIELDS = [
    "internal_council_id",
    "address",
    "postcode",
    "location",
    "council_id",
    "sample_uprn",
]

UPRN_TO_COUNCIL_CACHE = {}


class Command(BaseStationsImporter, CsvMixin):
    council_id = "ANN"  # This is a hack to make the command initialise
    stations_name = "eoni_stations.csv"
    stations_filetype = "csv"
    csv_encoding = "utf-8"
    eoni_csv_encoding = "latin-1"
    additional_report_councils = NIR_IDS

    def add_arguments(self, parser):
        parser.add_argument("eoni_csv", help="The path to the EONI export csv")
        parser.add_argument(
            "--stations-only",
            help="Don't process address, only update stations",
            action="store_true",
        )
        parser.add_argument(
            "--cleanup", help="Delete intermediate CSVs", action="store_true"
        )

    def handle(self, *args, **options):
        self.eoni_export_path = Path(options["eoni_csv"])
        self.eoni_data_root = self.eoni_export_path.absolute().parent

        self.paths = {
            "addresses": self.eoni_data_root / "eoni_address.csv",
            "uprn_to_council": self.eoni_data_root / "eoni_uprn_to_council.csv",
            "stations": self.eoni_data_root / "eoni_stations.csv",
        }
        self.stations_only = options.get("stations_only")
        self.pre_process_data()
        self.clear_old_data()
        self.copy_data()
        self.assign_uprn_to_councils()
        super().handle(*args, **options)
        if options.get("cleanup"):
            [path.unlink() for path in self.paths.values() if path.exists()]

    def teardown(self, council):
        # Only remove old polling stations, as the UPRN to Council table
        # is populated by this command previously, so deleting data form it
        # isn't useful.
        CustomFinder.objects.filter(area_code="N07000001").delete()
        PollingStation.objects.filter(council_id__in=NIR_IDS).delete()

    def get_base_folder_path(self):
        return str(self.eoni_data_root)

    def pre_process_data(self):
        if not self.stations_only:
            addresses = csv.DictWriter(
                open(self.paths["addresses"], "w", encoding=self.csv_encoding),
                fieldnames=ADDRESSES_FIELDS,
            )
            addresses.writeheader()
            uprns = csv.DictWriter(
                open(self.paths["uprn_to_council"], "w", encoding=self.csv_encoding),
                fieldnames=UPRN_FIELDS,
            )
            uprns.writeheader()

        stations = csv.DictWriter(
            open(self.paths["stations"], "w", encoding=self.csv_encoding),
            fieldnames=STATION_FIELDS,
        )
        stations.writeheader()
        station_data = {}

        with self.eoni_export_path.open(
            "r", encoding=self.eoni_csv_encoding
        ) as eoni_csv:
            # Do a single loop over the whole data file
            reader = csv.DictReader(eoni_csv)
            for row in reader:
                if not self.stations_only:
                    address_location = Point(
                        int(row["PRO_X_COR"]), int(row["PRO_Y_COR"]), srid=29902
                    )
                    address_location.transform(4326)
                    addresses.writerow(
                        {
                            "uprn": row["PRO_UPRN"].strip(),
                            "address": row["PRO_FULLADDRESS"].strip(),
                            "postcode": row["PRO_POSTCODE"].strip(),
                            "location": address_location.ewkt,
                            "addressbase_postal": "D",
                        }
                    )

                    uprns.writerow(
                        {
                            "uprn": row["PRO_UPRN"],
                            "lad": "EONI",
                            "polling_station_id": row["PREM_ID"],
                            "advance_voting_station_id": "NULL",
                        }
                    )

                station_data[row["PREM_ID"]] = {
                    "internal_council_id": row["PREM_ID"],
                    "postcode": row["PREM_POSTCODE"].strip(),
                    "address": f'{row["PREM_NAME"].strip()}, {row["PREM_FULLADDRESS"].strip()}',
                    "location_y": row["PREM_Y_COR"],
                    "location_x": row["PREM_X_COR"],
                    "council_id": "EONI",
                    "sample_uprn": row["PRO_UPRN"].strip(),
                }
            for internal_council_id, station in station_data.items():
                location = Point(
                    int(station.pop("location_x")),
                    int(station.pop("location_y")),
                    srid=29902,
                )
                location.transform(4326)
                station["location"] = location.ewkt
                stations.writerow(station)

    def clear_old_data(self):
        # Polling stations use reg codes
        PollingStation.objects.filter(council_id__in=NIR_IDS).delete()

        if not self.stations_only:
            # UprnToCouncil uses GSS codes
            NIR_AND_EONI = [
                c.geography.gss
                for c in Council.objects.filter(council_id__in=NIR_IDS).select_related(
                    "geography"
                )
            ]
            NIR_AND_EONI.append("EONI")  # Include fake 'EONI' gss just in case
            Address.objects.filter(uprntocouncil__lad__in=NIR_AND_EONI).delete()
            UprnToCouncil.objects.filter(lad__in=NIR_AND_EONI).delete()

    def copy_data(self):
        if not self.stations_only:
            cursor = connection.cursor()
            cursor.copy_expert(
                "COPY addressbase_address FROM STDIN CSV HEADER",
                open(self.paths["addresses"]),
            )
            cursor.copy_expert(
                "COPY addressbase_uprntocouncil FROM STDIN WITH NULL AS 'NULL' CSV HEADER",
                open(self.paths["uprn_to_council"]),
            )

    def assign_uprn_to_councils(self):
        ni_councils = Council.objects.filter(council_id__in=NIR_IDS).select_related(
            "geography"
        )
        for council in ni_councils:
            uprns_in_council = UprnToCouncil.objects.filter(lad="EONI").filter(
                uprn__location__within=council.geography.geography
            )
            uprns_in_council.update(lad=council.geography.gss)

    def station_record_to_dict(self, record):
        if not record.sample_uprn in UPRN_TO_COUNCIL_CACHE:
            UPRN_TO_COUNCIL_CACHE[record.sample_uprn] = Council.objects.get(
                identifiers__contains=[
                    UprnToCouncil.objects.get(uprn=record.sample_uprn).lad
                ]
            )
        station_council = UPRN_TO_COUNCIL_CACHE[record.sample_uprn]
        if station_council == self.council:
            return {
                "internal_council_id": getattr(record, "internal_council_id").strip(),
                "postcode": record.postcode,
                "address": record.address,
                "location": Point().from_ewkt(record.location),
            }

    def import_data(self):
        # We only need to import stations as addresses and UPRN to Council
        # is added using COPY
        ni_councils = Council.objects.filter(council_id__in=NIR_IDS)
        for council in ni_councils:
            self.council = council
            self.council_id = council.council_id
            self.stations = StationSet()
            self.import_polling_stations()
            self.stations.save()

    def check_in_council_bounds(self, station_record):
        if not station_record["postcode"].startswith("BT"):
            return False
        return True