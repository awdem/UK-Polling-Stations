from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "PEN"
    addresses_name = (
        "2024-05-02/2024-02-19T13:04:13.385326/Democracy_Club__02May2024 (2).tsv"
    )
    stations_name = (
        "2024-05-02/2024-02-19T13:04:13.385326/Democracy_Club__02May2024 (2).tsv"
    )
    elections = ["2024-05-02"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "10022950288",  # PEARL COTTAGE, ALMA ROAD, COLNE
            "10090961710",  # FLAT, TOWER BUILDINGS 2A, KEIGHLEY ROAD, COLNE
            "61014294",  # 117 EDWARD STREET, NELSON
            "100012398597",  # PLANTATION COTTAGE, GREENHEAD LANE, FENCE, BURNLEY
            "10024181464",  # FOSTERS LEAP BARN, TRAWDEN, COLNE
            "10024181048",  # WHITEMOOR BOTTOM FARM, WHITEMOOR ROAD, FOULRIDGE, COLNE
            "100012400306",  # BROWN HOUSE FARM, GISBURN OLD ROAD, BLACKO, NELSON
            "100012400306",  # BROWN HOUSE FARM, GISBURN OLD ROAD, BLACKO, NELSON
        ]:
            return None

        if record.addressline6 in [
            # splits
            "BB9 0RQ",
            "BB9 7YS",  # REEDYFORD COTTAGE, SCOTLAND ROAD, NELSON
            "BB8 7DN",  # GRASMERE CLOSE, COLNE
        ]:
            return None

        return super().address_record_to_dict(record)
