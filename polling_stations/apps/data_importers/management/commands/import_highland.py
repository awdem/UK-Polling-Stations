from data_importers.management.commands import BaseDemocracyCountsCsvImporter


class Command(BaseDemocracyCountsCsvImporter):
    council_id = "HLD"
    addresses_name = (
        "2024-11-21/2024-10-14T09:51:50.069320/Democracy Club - Polling Districts.csv"
    )
    stations_name = (
        "2024-11-21/2024-10-14T09:51:50.069320/Democracy Club - Polling Stations.csv"
    )
    elections = ["2024-11-21"]
    csv_encoding = "utf-16le"
    # This is a by-election so doesn't concern most of council
    # therefore, I'm leaving the GE exclusions as comments for future reference

    def station_record_to_dict(self, record):
        # # correcting obviously wrong point for:
        # # CROWN CHURCH, INVERNESS, KINGSMILLS ROAD, INVERNESS
        # if record.stationcode in [
        #     "I085",
        #     "I086",
        # ]:
        #     record = record._replace(xordinate="267087")

        # # SCOURIE COMMUNITY HALL, SCOURIE, LAIRG, SUTHERLAND, IV27 4TE
        # if record.stationcode == "C006":
        #     record = record._replace(xordinate="", yordinate="")

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        # uprn = record.uprn.strip().lstrip("0")

        # if (
        #     uprn
        #     in [
        #         "130150387",  # MILL COTTAGE A863 B884 JUNCTION - A850 JUNCTION, KILMUIR, DUNVEGAN
        #         "130186635",  # 1 MACFARLANE BUILDINGS, CRUACHAN PLACE, PORTREE
        #         "130131942",  # 3 WOODLAND PARK, CONTIN
        #         "130178830",  # 12 COUNTY PLACE, CULDUTHEL, INVERNESS
        #         "130197101",  # 4 BLACK ISLE VIEW, STRATTON, INVERNESS
        #         "130147608",  # NEWLANDS OF URCHANY, NAIRN
        #     ]
        # ):
        #     return None

        # if record.postcode in [
        #     # split
        #     "IV17 0QY",
        #     "IV23 2RW",
        # ]:
        #     return None
        return super().address_record_to_dict(record)
