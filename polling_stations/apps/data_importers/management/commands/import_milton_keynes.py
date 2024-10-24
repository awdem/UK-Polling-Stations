from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "MIK"
    addresses_name = (
        "2024-05-02/2024-03-04T09:26:46.650554/Democracy_Club__02May2024.tsv"
    )
    stations_name = (
        "2024-05-02/2024-03-04T09:26:46.650554/Democracy_Club__02May2024.tsv"
    )
    elections = ["2024-05-02"]
    csv_encoding = "windows-1252"
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "25091328",  # BROUGHTON MANOR, BROUGHTON, MILTON KEYNES
            "25092373",  # COOKSOE FARM, CHICHELEY, NEWPORT PAGNELL
            "10023651529",  # FLAT AT THE BLACK HORSE WOLVERTON ROAD, GREAT LINFORD, MILTON KEYNES
            "25096256",  # 26B STRATFORD ROAD, WOLVERTON, MILTON KEYNES
            "25041362",  # CAFE BUNGALOW, WATLING STREET, ELFIELD PARK, MILTON KEYNES
            "25088205",  # 5 STATION ROAD, WOBURN SANDS, MILTON KEYNES
            "10093919626",  # FLAT 126, SOLSTICE APARTMENTS, 801 SILBURY BOULEVARD, MILTON KEYNES
            "10093919687",  # FLAT 403, SOLSTICE APARTMENTS, 801 SILBURY BOULEVARD, MILTON KEYNES
            "10093919604",  # FLAT 104, SOLSTICE APARTMENTS, 801 SILBURY BOULEVARD, MILTON KEYNES
            "10093919616",  # FLAT 116, SOLSTICE APARTMENTS, 801 SILBURY BOULEVARD, MILTON KEYNES
            "10096063970",  # FLAT WESTBURY FARM FOXCOVERT ROAD, SHENLEY WOOD, MILTON KEYNES
            "25016686",  # ADDERSEY END, EAKLEY LANES, STOKE GOLDINGTON, NEWPORT PAGNELL
        ]:
            return None

        if record.addressline6 in [
            # splits
            "MK4 4EL",
            "MK4 4AG",
            "MK46 5AF",
            "MK17 8NB",
            "MK13 9DZ",
            "MK14 6DL",
            "MK13 7NH",
            "MK4 4AU",
            "MK46 4JS",
            # looks wrong
            "MK15 0DW",
            "MK17 8WS",
            "MK17 8WU",
            "MK17 8WT",
            "MK9 2HS",
        ]:
            return None

        return super().address_record_to_dict(record)
