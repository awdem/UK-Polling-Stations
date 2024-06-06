from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "ROT"
    addresses_name = (
        "2024-07-04/2024-06-06T14:29:03.086004/Democracy_Club__04July2024.tsv"
    )
    stations_name = (
        "2024-07-04/2024-06-06T14:29:03.086004/Democracy_Club__04July2024.tsv"
    )
    elections = ["2024-07-04"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "200000578516",  # FIELD COTTAGE, BISCAY LANE, WATH-UPON-DEARNE, ROTHERHAM
            "200000571433",  # FLAT, ABOVE JARVIS & WOMACK, STATION STREET, SWINTON, MEXBOROUGH
            "200000571411",  # THE VICARAGE, HIGHTHORN ROAD, KILNHURST, MEXBOROUGH
            "10095307545",  # 11 RERESBY PARK CLOSE, DALTON, ROTHERHAM
            "10000856639",  # 14 HOLLINGSWOOD WAY, SUNNYSIDE, ROTHERHAM
            "100050864180",  # 24 ROSEDALE WAY, SUNNYSIDE, ROTHERHAM
            "100050829576",  # 9 DALE HILL ROAD, MALTBY, ROTHERHAM
            "100050874821",  # WOODLAND LODGE, TICKHILL ROAD, MALTBY, ROTHERHAM
            "200000581738",  # ROCHE ABBEY MILL FARM, ROCHE ABBEY, MALTBY, ROTHERHAM
            "10091630508",  # LIVING ACCOMODATION SAXON HOTEL STATION ROAD, KIVETON PARK, ROTHERHAM
            "10032991676",  # 6 GREENSIDE AVENUE, KIVETON PARK, SHEFFIELD
            "100050896327",  # THE MARLINS, SUDBURY DRIVE, ASTON, SHEFFIELD
            "100050898298",  # KENVILLE, WEST LANE, AUGHTON, SHEFFIELD
            "200000582858",  # ULLEY BEECHES FARM, ULLEY BEECHES, THURCROFT, ROTHERHAM
            "10023213291",  # FLAT OVER BRINSWORTH BOARDING KENNELS BRINSWORTH ROAD, BRINSWORTH, ROTHERHAM
            "100050850916",  # 2 MANOR ROAD, BRINSWORTH, ROTHERHAM
            "100050818485",  # 55 BONET LANE, BRINSWORTH, ROTHERHAM
            "200000570018",  # HOWARTH LODGE, HOWARTH LANE, WHISTON, ROTHERHAM
            "100050814600",  # 97 BADSLEY MOOR LANE, ROTHERHAM
            "100050814598",  # 95 BADSLEY MOOR LANE, ROTHERHAM
            "10093477945",  # LIVING ACCOMODATION RED LION HOTEL RED LION YARD, ROTHERHAM TOWN CENTRE, ROTHERHAM
            "10093478098",  # FIRST FLOOR FLAT WHARF HOUSE BRIDGE STREET, ROTHERHAM TOWN CENTRE, ROTHERHAM
            "10093479098",  # LIVING ACCOMMODATION THE BRIDGE INN GREASBROUGH ROAD, NORTHFIELD, ROTHERHAM
            "100052101595",  # LOCK HOUSE, BRINSWORTH STREET, ROTHERHAM
            "10095308818",  # FLAT UNIT 2 PARKGATE COMPLEX RAWMARSH ROAD, NORTHFIELD, ROTHERHAM
            "10093479180",  # LIVING ACCOMMODATION PARK HOTEL BADSLEY MOOR LANE, HERRINGTHORPE, ROTHERHAM
            "100050832618",  # 2 EAST ROAD, ROTHERHAM
            "100052091706",  # HARDWICK GRANGE COTTAGE, HARDWICK LANE, ASTON, SHEFFIELD
            "100050887718",  # HARDWICK GRANGE FARM, HARDWICK LANE, ASTON, SHEFFIELD
            "10023213316",  # ORCHARD HOUSE, WORKSOP ROAD, TODWICK, SHEFFIELD
            "100050861724",  # RAVENBROOK, RAVENFIELD LANE, HOOTON ROBERTS, ROTHERHAM
            "200000575438",  # STONE FARM, STONE, MALTBY, ROTHERHAM
            "200000580669",  # THE BARN, ROCHE ABBEY, MALTBY, ROTHERHAM
            "200000580689",  # MILL HOUSE, ROCHE ABBEY, MALTBY, ROTHERHAM
            "200000582514",  # MILL COTTAGE, ROCHE ABBEY, MALTBY, ROTHERHAM
            "100050821009",  # 32 BROADWAY, BRINSWORTH, ROTHERHAM
            "100050841025",  # 26 HARDWICK STREET, ROTHERHAM
            "100052107725",  # RED GABLES, RAVENFIELD LANE, HOOTON ROBERTS, ROTHERHAM
            "10032993058",  # 1B LLOYD STREET, PARKGATE, ROTHERHAM
            "10096739470",  # 5 COLLIERS PLACE, DINNINGTON, ROTHERHAM
            "200000575374",  # COTTERHILL WOODS FARM, BLACK LANE, WOODSETTS, WORKSOP
            "10093480494",  # FLAT AT ASTON PARK FISHERIES ASTON WAY, ASTON, ROTHERHAM
        ]:
            return None

        if record.addressline6 in [
            # splits
            "S64 8PG",
            # suspect
            "S63 7LN",
            "S64 8BD",
            "S65 4FP",
            "S26 4XB",
            "S25 2DR",
        ]:
            return None

        return super().address_record_to_dict(record)
