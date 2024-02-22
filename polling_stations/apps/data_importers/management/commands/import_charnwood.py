from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter
from django.contrib.gis.geos import Point


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "CHA"
    addresses_name = "2024-05-02/2024-02-22T12:52:09.139310/Democracy_Club__02May2024 - Charnwood Borough Council.tsv"
    stations_name = "2024-05-02/2024-02-22T12:52:09.139310/Democracy_Club__02May2024 - Charnwood Borough Council.tsv"
    elections = ["2024-05-02"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")
        if uprn in [
            "10070073939",  # MANAGERS ACCOMMODATION 109 LEICESTER ROAD, MOUNTSORREL
            "10091071561",  # THE OLD FARM HOUSE, SCHOOL LANE, BIRSTALL, LEICESTER
            "100030454789",  # 230 NARROW LANE, WYMESWOLD, LOUGHBOROUGH
            "100030439104",  # 2 CHURCH STREET, BARROW UPON SOAR, LOUGHBOROUGH
            "100030439106",  # 4 CHURCH STREET, BARROW UPON SOAR, LOUGHBOROUGH
            "100030446529",  # 70 HIGH STREET, BARROW UPON SOAR, LOUGHBOROUGH
            "100032039889",  # 27 MARKET PLACE, LOUGHBOROUGH
            "200000845475",  # HAMILTON GROUND FARM, HAMILTON LANE, SCRAPTOFT, LEICESTER
            "100030447889",  # ROECLIFFE FARM, JOE MOORES LANE, WOODHOUSE EAVES, LOUGHBOROUGH
            "100030433587",  # MUCKLIN LODGE, MAIN STREET, WOODTHORPE, LOUGHBOROUGH
            "10091071652",  # FARMHOUSE HOLYWELL FARM ASHBY ROAD, LOUGHBOROUGH
            "10023775540",  # FARMHOUSE HURST FARM ASHBY ROAD, LOUGHBOROUGH
            "100030416689",  # 1 GEORGE STREET, ANSTEY, LEICESTER
            "100030410787",  # 146 BARKBY ROAD, SYSTON, LEICESTER
            "100032069971",  # 383 FOSSE WAY, RATCLIFFE ON THE WREAKE, LEICESTER
            "100030416263",  # 381 FOSSE WAY, RATCLIFFE ON THE WREAKE, LEICESTER
            "100030468031",  # 176 WOODHOUSE ROAD, QUORN, LOUGHBOROUGH
            "100030468032",  # 178 WOODHOUSE ROAD, QUORN, LOUGHBOROUGH
            "100030438667",  # 76 CHAVENEY ROAD, QUORN, LOUGHBOROUGH
            "100032042167",  # PAUDY COTTAGE, MELTON ROAD, BARROW UPON SOAR, LOUGHBOROUGH
            "10013595577",  # LOUGHBOROUGH UNIVERSITY, FALKNER EGGINGTON COURT, LOUGHBOROUGH
            "200000837466",  # 380 BRADGATE ROAD, NEWTOWN LINFORD, LEICESTER
            "100030453672",  # FARMHOUSE CLIFF FARM 120 MELTON ROAD, BURTON ON THE WOLDS
            "100030414459",  # OSIERS VILLA, SYSTON ROAD, COSSINGTON, LEICESTER
            "10094174031",  # NARROWBOAT THE LAST CRUSADE SILEBY MARINA MILL LANE, SILEBY
            "100030454544",  # THE OLD MILL, MILL LANE, SILEBY, LOUGHBOROUGH
            "100030419313",  # LAKESIDE COTTAGE, KINCHLEY LANE, ROTHLEY, LEICESTER
        ]:
            return None

        if record.addressline6 in [
            # splits
            "LE11 5EB",
            "LE11 5JQ",
            "LE7 7GA",  # BRADGATE ROAD, CROPSTON, LEICESTER
            "LE11 5FJ",  # COTTON WAY, LOUGHBOROUGH
            "LE12 7SF",  # HOBBS WICK, SILEBY, LOUGHBOROUGH
        ]:
            return None
        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        rec = super().station_record_to_dict(record)

        # more accurate point for St Theresas Church Hall, 53 Front Street, Birstall, LE4 4DQ
        if rec["internal_council_id"] == "11072":
            rec["location"] = Point(-1.1182210, 52.675904, srid=4326)

        return rec
