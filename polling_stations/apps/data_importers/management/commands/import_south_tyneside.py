from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "STY"
    addresses_name = (
        "2024-05-02/2024-03-12T17:14:20.914959/Democracy_Club__02May2024.tsv"
    )
    stations_name = (
        "2024-05-02/2024-03-12T17:14:20.914959/Democracy_Club__02May2024.tsv"
    )
    elections = ["2024-05-02"]
    csv_delimiter = "\t"

    def station_record_to_dict(self, record):
        # coordinate fix from council:
        # Bilton Hall Community Trust, Low Simonside Community Centre, Taunton Avenue, Jarrow, NE32 3RT
        if record.polling_place_id == "5403":
            record = record._replace(
                polling_place_easting="434136",
                polling_place_northing="564254",
            )

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "200000000962",  # 2 CLIFF COTTAGES, QUAY CORNER AVENUE, JARROW
            "200000000963",  # CLIFF HOUSE, QUAY CORNER AVENUE, JARROW
            "200000000961",  # 1 CLIFF COTTAGES, QUAY CORNER AVENUE, JARROW
            "103001354",  # MANAGERS ACCOMMODATION THE STORYBOOK ABINGDON WAY, SOUTH TYNESIDE, BOLDON COLLIERY
            "200000006403",  # THE COTTAGE, WHITBURN MOORS FARM, SUNDERLAND ROAD, SUNDERLAND
        ]:
            return None

        if record.addressline6 in [
            # splits
            "NE31 2EA",
            "NE31 2XF",
            "NE34 8AE",
        ]:
            return None

        return super().address_record_to_dict(record)
