from data_importers.management.commands import BaseDemocracyCountsCsvImporter


class Command(BaseDemocracyCountsCsvImporter):
    council_id = "HLD"
    addresses_name = "2024-07-04/2024-06-17T14:00:37.781062/HLD_districts_combined.csv"
    stations_name = "2024-07-04/2024-06-17T14:00:37.781062/HLD_stations_combined.csv"
    elections = ["2024-07-04"]

    def station_record_to_dict(self, record):
        # correcting obviously wrong point for:
        # CROWN CHURCH, INVERNESS, KINGSMILLS ROAD, INVERNESS
        if record.stationcode in [
            "I085",
            "I086",
        ]:
            record = record._replace(xordinate="267087")

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if uprn in [
            "130150387",  # MILL COTTAGE A863 B884 JUNCTION - A850 JUNCTION, KILMUIR, DUNVEGAN
            "130186635",  # 1 MACFARLANE BUILDINGS, CRUACHAN PLACE, PORTREE
            "130131942",  # 3 WOODLAND PARK, CONTIN
            "130178830",  # 12 COUNTY PLACE, CULDUTHEL, INVERNESS
            "130197101",  # 4 BLACK ISLE VIEW, STRATTON, INVERNESS
            "130147608",  # NEWLANDS OF URCHANY, NAIRN
        ]:
            return None

        if record.postcode in [
            # split
            "IV17 0QY",
            "IV23 2RW",
        ]:
            return None
        return super().address_record_to_dict(record)
