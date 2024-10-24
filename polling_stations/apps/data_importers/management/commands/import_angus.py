from data_importers.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "ANS"
    addresses_name = "2024-04-25/2024-03-12T07:20:19.214321/Eros_SQL_Output005.csv"
    stations_name = "2024-04-25/2024-03-12T07:20:19.214321/Eros_SQL_Output005.csv"
    elections = ["2024-04-25"]

    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if uprn in [
            "117080095",  # LOWNIE HILL COTTAGE, FORFAR
            "117080326",  # UPPER TULLOES FARM, FORFAR
            "117087696",  # WOODSIDE, NETHER TULLOES FARM, FORFAR
            "117119577",  # THE BUNGALOW ACCESS FROM MID MAINS OF CONONSYTH TO SOUTH MAINS OF CONONSYTH, SOUTH MAINS OF CONONSYTH, ARBROATH
            "117120941",  # KNOWES FARM, ARBROATH
            "117081204",  # KNOWES FARM BUNGALOW, ARBROATH
            "117101108",  # MONTREATHMONT COTTAGE, FORFAR
        ]:
            return None

        if record.housepostcode in [
            # splits
            "DD8 2TJ",
        ]:
            return None

        return super().address_record_to_dict(record)
