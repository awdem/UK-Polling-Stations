from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "TOB"
    addresses_name = "2024-07-04/2024-06-20T10:46:28.307156/TOB_combined.tsv"
    stations_name = "2024-07-04/2024-06-20T10:46:28.307156/TOB_combined.tsv"
    elections = ["2024-07-04"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if (
            uprn
            in [
                "100040529632",  # 16 OLD TORQUAY ROAD, PAIGNTON
                "10024003083",  # 30 SHORTON ROAD, PAIGNTON
                "100040532454",  # 28 SHORTON ROAD, PAIGNTON
                "100040513377",  # MILTON ORCHARD, MILTON STREET, BRIXHAM
                "100040515861",  # REDWELLS, SOUTHDOWN HILL, BRIXHAM
                "100040513359",  # BEL-OMBRE, MILTON STREET, BRIXHAM
                "10024001656",  # GATEHOUSE COTTAGE MUDSTONE LANE, BRIXHAM
                "10093140000",  # 11 REA BARN ROAD, BRIXHAM
                "100040509069",  # 89 BOLTON STREET, BRIXHAM
                "100040509951",  # 64 COPYTHORNE ROAD, BRIXHAM
                "100040509950",  # 62 COPYTHORNE ROAD, BRIXHAM
                "100040509722",  # 1A CHURCH HILL EAST, BRIXHAM
                "100040514040",  # 110 NORTH BOUNDARY ROAD, BRIXHAM
                "100040534758",  # 187 TOTNES ROAD, PAIGNTON
                "100040512567",  # 48 LICHFIELD DRIVE, BRIXHAM
                "100040510175",  # THE STATION GUEST HOUSE, DARTMOUTH ROAD, CHURSTON FERRERS, BRIXHAM
                "100040534883",  # ZOO AND GARDENS NORTH LODGE TOTNES ROAD, PAIGNTON
                "10000010093",  # CROWN & ANCHOR COTTAGE, CROWN & ANCHOR WAY, PAIGNTON
                "100040536537",  # 114 WINNER STREET, PAIGNTON
                "100040534320",  # 133 TORQUAY ROAD, PAIGNTON
                "10093142379",  # 73A BLATCHCOMBE ROAD, PAIGNTON
                "100040532457",  # 32 SHORTON ROAD, PRESTON, PAIGNTON
                "100040532460",  # 36 SHORTON ROAD, PRESTON, PAIGNTON
                "10094527862",  # BAY VISTA, COCKINGTON LANE, PRESTON, PAIGNTON
                "100040525248",  # 42 HEADLAND PARK ROAD, PAIGNTON
                "100040552641",  # 1 PENNYS COTTAGE, PENNYS HILL, TORQUAY
                "100040543734",  # 53 FOREST ROAD, TORQUAY
                "10024003109",  # 22B LOWER SHIRBURN ROAD, TORQUAY
                "100040557811",  # 36 STUDLEY ROAD, TORQUAY
                "200001110813",  # WALDERLEA, CARY PARK, TORQUAY
                "10093141340",  # FLAT 2 ODDICOMBE HALL BABBACOMBE DOWNS ROAD, TORQUAY
                "100040537792",  # 44A BABBACOMBE ROAD, TORQUAY
                "100040537793",  # 44B BABBACOMBE ROAD, TORQUAY
                "100040541181",  # 34 CHURCH ROAD, ST. MARYCHURCH, TORQUAY
                "10093141957",  # FLAT 2, CORNERSTONE HOUSE, TEIGNMOUTH ROAD, TORQUAY
                "100040538271",  # 1 BARCHINGTON AVENUE, TORQUAY
                "100041199418",  # OLD SCHOOL HOUSE, ALSTON LANE, CHURSTON FERRERS, BRIXHAM
                "200002083269",  # PONTOON ADJ PRINCESS PIER, PONTOON ADJ PRINCESS PIER TORBAY ROAD, TORQUAY
                "100040548281",  # HATLEY ST. GEORGE, LINCOMBE DRIVE, TORQUAY
                "100041187861",  # THE COTTAGE, LOWER ERITH ROAD, TORQUAY
                "10094526711",  # BARWOOD MEWS, LOWER WARBERRY ROAD, TORQUAY
                "100040538743",  # DOWNSVIEW CORNER, BEDFORD ROAD, TORQUAY
                "100040551304",  # 91 NUT BUSH LANE, TORQUAY
                "100040551303",  # 89 NUT BUSH LANE, TORQUAY
                "100040537642",  # HIGH VIEW LODGE, AVENUE ROAD, TORQUAY
                "100040549481",  # 1D MAGDALENE ROAD, TORQUAY
                "100041198763",  # 308 DARTMOUTH ROAD, PAIGNTON
                "100040541253",  # CHERRY BLOSSOM FARM, CLADDON LANE, MAIDENCOMBE, TORQUAY
                "100040554887",  # PROTEA, SEAWAY LANE, TORQUAY
                "10094529096",  # THE COURTYARD APARTMENT, 306 TORQUAY ROAD, PAIGNTON
            ]
        ):
            return None

        if record.addressline6 in [
            "TQ3 3NU",  # split
            # looks wrong
            "TQ1 4QZ",
            "TQ5 8EJ",
            "TQ5 8AW",
            "TQ5 0LB",
            "TQ3 3QG",
            "TQ3 3QE",
            "TQ2 5BU",
        ]:
            return None

        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        # The following station postcode has been confirmed by the council:

        # Beefeater Restaurant, Whiterock, Long Road South, Paignton TQ4 7RZ
        if record.polling_place_id == "10315":
            record = record._replace(polling_place_postcode="TQ4 7AZ")
        return super().station_record_to_dict(record)
