from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "RUG"
    addresses_name = (
        "2024-05-02/2024-03-19T15:58:18.755378/Democracy_Club__02May2024.tsv"
    )
    stations_name = (
        "2024-05-02/2024-03-19T15:58:18.755378/Democracy_Club__02May2024.tsv"
    )
    elections = ["2024-05-02"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        if record.addressline6 in [
            # suspect
            "CV22 7YF",
            "CV22 7ZX",
        ]:
            return None
        return super().address_record_to_dict(record)
