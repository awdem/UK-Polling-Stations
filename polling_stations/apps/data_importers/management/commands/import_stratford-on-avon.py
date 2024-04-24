from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter
from django.contrib.gis.geos import Point


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "STR"
    addresses_name = (
        "2024-05-02/2024-03-18T15:53:02.626241/Democracy_Club__02May2024 (20).tsv"
    )
    stations_name = (
        "2024-05-02/2024-03-18T15:53:02.626241/Democracy_Club__02May2024 (20).tsv"
    )
    elections = ["2024-05-02"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "100071512710",  # DARLINGSCOTT HILL, DARLINGSCOTE ROAD, SHIPSTON-ON-STOUR
            "100071244138",  # WIL HAVEN, DARLINGSCOTE ROAD, SHIPSTON-ON-STOUR
            "10023584621",  # DITCHFORD FRIARY MANOR, TIDMINGTON, SHIPSTON-ON-STOUR
            "10023584622",  # GARDEN COTTAGE DITCHFORD FRIARY DITCHFORD ROAD, TIDMINGTON
            "10023584685",  # LITTLE KIRBY, KIRBY FARM, WHATCOTE, SHIPSTON-ON-STOUR
            "100071241496",  # GLENDALE, CAMP LANE, WARMINGTON, BANBURY
            "100071241501",  # RIDGE HOUSE, CAMP LANE, WARMINGTON, BANBURY
            "10023582389",  # EGGE COTTAGE, EDGEHILL, BANBURY
            "10023387192",  # BARN VIEW, KYTE GREEN, HENLEY-IN-ARDEN
            "10094564878",  # FLAT 1 RIVERSIDE LODGE, CLIFFORD MILL, CLIFFORD ROAD, STRATFORD-UPON-AVON
            "10094564879",  # FLAT 2 RIVERSIDE LODGE, CLIFFORD MILL, CLIFFORD ROAD, STRATFORD-UPON-AVON
            "10094564880",  # FLAT 3 RIVERSIDE LODGE, CLIFFORD MILL, CLIFFORD ROAD, STRATFORD-UPON-AVON
            "10094564881",  # FLAT 4 RIVERSIDE LODGE, CLIFFORD MILL, CLIFFORD ROAD, STRATFORD-UPON-AVON
            "10094564882",  # FLAT 5 RIVERSIDE LODGE, CLIFFORD MILL, CLIFFORD ROAD, STRATFORD-UPON-AVON
            "10094564883",  # FLAT 6 RIVERSIDE LODGE, CLIFFORD MILL, CLIFFORD ROAD, STRATFORD-UPON-AVON
            "10023382223",  # RADBROOK EDGE, PRESTON ON STOUR, STRATFORD-UPON-AVON
            "100071244137",  # WHADDON FARM, DARLINGSCOTE ROAD, SHIPSTON-ON-STOUR
            "100071249075",  # GREENFIELDS FARM, HARDWICK LANE, OUTHILL, STUDLEY
            "10023580629",  # OX HOUSE FARM, COMBROOK, WARWICK
            "100071241494",  # BATTLE LODGE, CAMP LANE, WARMINGTON, BANBURY
            "100071241504",  # YENTON, CAMP LANE, WARMINGTON, BANBURY
            "100071491317",  # HENLEY HOTEL, TANWORTH LANE, HENLEY-IN-ARDEN
            "10094567022",  # 32 LANCASTER WAY, SHACKLETON VILLAGE
            "10023387972",  # AVON BANK HOUSE, CHURCH BANK, BINTON ROAD, WELFORD ON AVON, STRATFORD-UPON-AVON
        ]:
            return None

        if record.addressline6 in [
            # splits
            "CV37 8LT",
            # looks wrong
            "CV37 5AF",
        ]:
            return None

        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        # Station name change requested by council
        # OLD: The Avenue Club, Avenue Farm, Stratford-upon-Avon, CV37 0HR
        # NEW: Venture House, Avenue Farm, Birmingham Road, Stratford-upon-Avon, CV37 0HR
        if record.polling_place_id == "11601":
            record = record._replace(
                polling_place_name="Venture House",
                polling_place_address_1="Avenue Farm",
                polling_place_address_2="Birmingham Road",
                polling_place_address_3="",
                polling_place_address_4="Stratford-upon-Avon",
                polling_place_postcode="CV37 0HR",
            )

        rec = super().station_record_to_dict(record)

        # more accurate point for: Alcester Guide and Scout Centre, 28 Moorfield Road, Alcester, B49 5DA
        if rec["internal_council_id"] == "11550":
            rec["location"] = Point(-1.5998000, 52.191589, srid=4326)

        # more accurate point for: Wellesbourne Sports and Community Centre, Loxley Close, Wellesbourne, CV35 9RU
        if rec["internal_council_id"] == "11607":
            rec["location"] = Point(-1.871989, 52.216317, srid=4326)

        return rec
