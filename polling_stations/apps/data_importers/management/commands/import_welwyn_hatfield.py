from data_importers.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "WEW"
    addresses_name = "2023-05-04/2023-04-07T12:35:07.022003/Eros_SQL_Output002.csv"
    stations_name = "2023-05-04/2023-04-07T12:35:07.022003/Eros_SQL_Output002.csv"
    elections = ["2023-05-04"]
