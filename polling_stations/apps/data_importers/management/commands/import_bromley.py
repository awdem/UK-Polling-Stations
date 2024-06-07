from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "BRY"
    addresses_name = (
        "2024-07-04/2024-06-07T17:10:44.038104/Democracy_Club__04July2024.tsv"
    )
    stations_name = (
        "2024-07-04/2024-06-07T17:10:44.038104/Democracy_Club__04July2024.tsv"
    )
    elections = ["2024-07-04"]
    csv_encoding = "windows-1252"
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "10013150913",  # 87A LENNARD ROAD, LONDON
            "100020423411",  # 185 GREEN LANE, CHISLEHURST
            "100020423410",  # 183 GREEN LANE, CHISLEHURST
            "100020423673",  # 1C HIGH STREET, CHISLEHURST
            "100022899077",  # 88A HIGH STREET, ORPINGTON
            "100023390817",  # R&S BUILDERS LTD, 18 MAIN ROAD, BIGGIN HILL, WESTERHAM
            "100020373117",  # ANDERTON KING CLOCKMAKER, 48 BURNHILL ROAD, BECKENHAM
            "100020428160",  # GLEBE COTTAGE, CHURCH ROAD, KESTON
            "10003619831",  # STRATTMORE, SILVERSTEAD LANE, WESTERHAM
            "100020475660",  # WOODLANDS, SKEET HILL LANE, ORPINGTON
            "100022898831",  # WOODSIDE FARM, SKEET HILL LANE, ORPINGTON
            "100020475349",  # LOWER HOOK FARMHOUSE, SHIRE LANE, ORPINGTON
        ]:
            return None

        if record.addressline6 in [
            # splits
            "BR2 7AH",
            # looks wrong
            "BR3\xa04UA",
            "BR1\xa03FR",
            "BR3\xa04UB",
            "BR3\xa01AJ",
            "BR3\xa03QJ",
        ]:
            return None

        return super().address_record_to_dict(record)
