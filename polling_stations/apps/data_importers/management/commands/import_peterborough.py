from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "PTE"
    addresses_name = (
        "2022-05-05/2022-03-24T09:40:07.399960/Democracy_Club__05May2022.tsv"
    )
    stations_name = (
        "2022-05-05/2022-03-24T09:40:07.399960/Democracy_Club__05May2022.tsv"
    )
    elections = ["2022-05-05"]
    csv_delimiter = "\t"

    def station_record_to_dict(self, record):

        # Hampton Leisure Centre Clayburn Road Hampton Vale Peterborough PE7 8HQ
        if record.polling_place_id == "9249":
            record = record._replace(polling_place_postcode="PE7 8HG")

        # St Andrews Church Russell Hill Thornhaugh Peterborough PE6 6NW
        if record.polling_place_id == "9397":
            record = record._replace(polling_place_postcode="")

        # Hampton Community Sports Association, PE7 8DN
        if record.polling_place_id == "9367":
            record = record._replace(polling_place_postcode="")
        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "10094542529",  # 64 GREENFIELD WAY, HAMPTON WATER, PETERBOROUGH
        ]:
            return None

        if record.addressline6 in [
            "PE7 0LE",
        ]:
            return None

        return super().address_record_to_dict(record)
