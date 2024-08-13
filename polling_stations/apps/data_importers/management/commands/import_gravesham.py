from data_importers.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "GRA"
    addresses_name = "2024-07-04/2024-05-31T16:02:47.088690/Eros_SQL_Output001.csv"
    stations_name = "2024-07-04/2024-05-31T16:02:47.088690/Eros_SQL_Output001.csv"
    elections = ["2024-07-04"]

    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if (
            uprn
            in [
                "100060927470",  # 88 DOVER ROAD, NORTHFLEET, GRAVESEND
                "100060927472",  # 90 DOVER ROAD, NORTHFLEET, GRAVESEND
                "100060927474",  # 92 DOVER ROAD, NORTHFLEET, GRAVESEND
                "10012012612",  # FLAT ABOVE THE SHIP AND LOBSTER MARK LANE, GRAVESEND
                "100060938783",  # 162 OLD ROAD EAST, GRAVESEND
                "100060933575",  # 1 JUBILEE CRESCENT, GRAVESEND
                "100060933577",  # 3 JUBILEE CRESCENT, GRAVESEND
                "100060944345",  # RECTORY COTTAGE, SPRINGHEAD ENTERPRISE PARK, SPRINGHEAD ROAD, NORTHFLEET, GRAVESEND
                "100060939369",  # 36-38 OVERCLIFFE, GRAVESEND
                "100062310253",  # 99B PELHAM ROAD, GRAVESEND
                "100062310252",  # 99A PELHAM ROAD, GRAVESEND
                "100062309977",  # 99C PELHAM ROAD, GRAVESEND
                "10012012658",  # THE SPRINGS WATLING STREET, GRAVESEND
                "10012013951",  # LEYWOOD COTTAGE, LEYWOOD ROAD, MEOPHAM, GRAVESEND
                "100060934936",  # OAKLANDS, LEYWOOD ROAD, MEOPHAM, GRAVESEND
                "100060934937",  # PRIMROSE COTTAGE, LEYWOOD ROAD, MEOPHAM, GRAVESEND
                "100062063828",  # 1 GATEHOUSE COTTAGE, CHURCH ROAD, IFIELD, COBHAM, GRAVESEND
                "100060938600",  # YEW TREES, OAKENDEN ROAD, LUDDESDOWN, GRAVESEND
                "10012013958",  # WOODHILL FARM, BRIMSTONE HILL, MEOPHAM, GRAVESEND
                "10012014473",  # BRIMSTONE WOOD, BRIMSTONE HILL, MEOPHAM, GRAVESEND
                "10012014411",  # BRIMSTONE LODGE, BRIMSTONE HILL, MEOPHAM, GRAVESEND
            ]
        ):
            return None

        if record.housepostcode.strip() in [
            # splits
            "ME3 7NB",
            # suspect
            "DA12 4JS",  # GREGORYS CRESCENT, GRAVESEND
            "DA13 0XA",  # GOLD STREET, LUDDESDOWN, GRAVESEND
            "DA13 0UF",  # WHITE HORSE ROAD, MEOPHAM, GRAVESEND
            "DA13 0UA",  # SWANSWOOD FARM, HARVEL ROAD, MEOPHAM, GRAVESEND
            "DA13 0RN",  # HARVEL ROAD, MEOPHAM, GRAVESEND
            "DA3 7AL",  # SHIPLEY HILL COTTAGES, LONGFIELD ROAD, LONGFIELD
        ]:
            return None

        return super().address_record_to_dict(record)
