from data_importers.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "SRI"
    addresses_name = (
        "2022-05-05/2022-03-30T11:37:35.084389/polling_station_export-2022-03-24-2.csv"
    )
    stations_name = (
        "2022-05-05/2022-03-30T11:37:35.084389/polling_station_export-2022-03-24-2.csv"
    )
    elections = ["2022-05-05"]

    def station_record_to_dict(self, record):
        # Warning for BUCKSHAW VILLAGE COMMUNITY CENTRE (2-buckshaw-village-community-centre)
        # being outside the target council area, but it's fine.

        # COUPE GREEN PRIMARY SCHOOL, COUPE GREEN, HOGHTON, PRESTON
        if record.pollingstationnumber == "62":
            record = record._replace(pollingstationpostcode="PR5 0JR")  # was PR5 OJR

        # HIGHER  WALTON COMMUNITY CENTRE, OFF HIGHER  WALTON ROAD, HIGHER WALTON, PRESTON
        if record.pollingstationnumber == "64":
            record = record._replace(pollingstationpostcode="PR5 4HU")  # was PR5 4HV

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        if record.housepostcode in ["PR5 5AU", "PR5 4TB"]:
            return None  # split
        return super().address_record_to_dict(record)
