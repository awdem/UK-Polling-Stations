from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "RED"
    addresses_name = (
        "2022-05-05/2022-03-10T16:07:01.999058/Democracy_Club__05May2022.CSV"
    )
    stations_name = (
        "2022-05-05/2022-03-10T16:07:01.999058/Democracy_Club__05May2022.CSV"
    )
    elections = ["2022-05-05"]
