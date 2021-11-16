from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "RIH"
    addresses_name = "2021-11-08T12:16:18.989510/Democracy_Club__25November2021.CSV"
    stations_name = "2021-11-08T12:16:18.989510/Democracy_Club__25November2021.CSV"
    elections = ["2021-11-25"]

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "10004781106",  # CALVERTS NOOK, THE GAITS, GAYLE, HAWES
            "10034642865",  # LOW CAMMS HOUSE, ASKRIGG, LEYBURN
            "10034645243",  # COVER BRIDGE BUNGALOW, EAST WITTON, LEYBURN
            "10034644048",  # ELLENGARTH, GARRISTON, LEYBURN
            "10090348320",  # OHLSON HOUSE BARDEN LANE, BARDEN
            "10012781811",  # NEW FARM HOUSE CRAGGS LANE FARM CRAGGS LANE, TUNSTALL
            "100051959949",  # GARDENERS COTTAGE RICHMOND ROAD, HIPSWELL
            "10034646179",  # STOTTERGILL GUNING LANE TO GUNNERSIDE, SATRON, GUNNERSIDE
            "10034641250",  # THEAS COTTAGE, SATRON, GUNNERSIDE, RICHMOND
            "10012784013",  # SATRON FARM, GUNNERSIDE, RICHMOND
            "10012784008",  # GILL HEAD, GUNNERSIDE, RICHMOND
            "10034642031",  # BENTS HOUSE, LOW ROW, RICHMOND
            "10034643612",  # THE BARN SPRING END FARM CRACKPOT TO GUNNERSIDE, LOW ROW
            "10034643695",  # BARNACRES BUNGALOW, SKEEBY, RICHMOND
            "10004782465",  # SKEEBY LODGE, SCURRAGH LANE, SKEEBY, RICHMOND
            "10034644313",  # GREENBERRY FARM, SOUTH COWTON, NORTHALLERTON
            "10004781639",  # THE OLD SMITHY, HALNABY GRANGE, NORTH COWTON, NORTHALLERTON
            "10034649653",  # CARAVAN AT STONEY STOOPS SCOTCH CORNER TO APPLEBY TRUNK ROAD, EAST LAYTON
            "10034645690",  # SAUNDERS HOUSE FARM SCOTCH CORNER TO APPLEBY TRUNK ROAD, EAST LAYTON
            "10034645324",  # RIVERBANK COTTAGE, ALDBROUGH ST. JOHN, RICHMOND
            "10012782380",  # BOBBIN MILL COTTAGE, GARRISTON, LEYBURN
            "10034644167",  # THE OLD BLACKSMITHS SHOP VILLAGE STREETS NORTH OF GREEN, REETH
            "10090348313",  # THE HAMMOND WAITLANDS LANE, RAVENSWORTH
        ]:
            return None
        if record.addressline6 in [
            "DL8 3HJ",
            "DL8 4LY",
            "DL10 4SN",
            "DL10 7AZ",
            "DL10 7ES",
            "DL11 6NT",
            "DL11 6RE",
            "DL11 7TF",
            "DL8 3EA",
            "DL8 4AS",
            "DL8 4DH",
            "DL9 3NJ",
            "DL9 4JA",
            "DL9 4LA",
            "DL9 4NN",
            "DL9 4RT",
            "DL10 4TJ",
            "DL11 6JJ",
            "DL8 3DF",
            "DL8 3PN",
            "DL116AB",
        ]:
            return None

        return super().address_record_to_dict(record)

    #
    def station_record_to_dict(self, record):
        # 'Cleasby and Stapleton Village Hall, Cleasby,  ' (id: 7527)
        if record.polling_place_id == "7527":
            record = record._replace(polling_place_postcode="DL2 2RA")

        # 'Colburn Village Hall, Colburn Lane, Colburn, DL9 4LS' (id: 7558)
        if record.polling_place_id == "7558":
            record = record._replace(polling_place_postcode="DL9 4LZ")

        # 'North Cowton Village Hall, North Cowton, Northallerton, DL7 0HR' (id: 7569)
        if record.polling_place_id == "7569":
            record = record._replace(polling_place_postcode="DL7 0HF")

        # 'Eppleby Village Hall, Chapel Row, Eppleby, DL11 7AP' (id: 7661)
        if record.polling_place_id == "7661":
            record = record._replace(polling_place_postcode="DL11 7AU")

        # 'Aysgarth Village Hall, Main Street, Aysgarth, DL8 3AH' (id: 7515)
        if record.polling_place_id == "7515":
            record = record._replace(polling_place_postcode="DL8 3AD")

        # 'Bainbridge Village Hall, Bainbridge,  ' (id: 7519)
        if record.polling_place_id == "7519":
            record = record._replace(polling_place_postcode="DL8 3EF")

        return super().station_record_to_dict(record)
