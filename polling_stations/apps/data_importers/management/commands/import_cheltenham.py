from addressbase.models import Address
from data_importers.management.commands import BaseHalaroseCsvImporter
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseHalaroseCsvImporter):
    council_id = "CHT"
    addresses_name = "2024-05-02/2024-03-15T09:36:32.391996/Eros_SQL_Output009.csv"
    stations_name = "2024-05-02/2024-03-15T09:36:32.391996/Eros_SQL_Output009.csv"
    elections = ["2024-05-02"]

    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if uprn in [
            "100121229562",  # THE MEWS, BACK MONTPELLIER TERRACE, CHELTENHAM
            "200002684616",  # 49A BACK MONTPELLIER TERRACE, CHELTENHAM
            "100120413433",  # FLAT, 19 SUFFOLK ROAD, CHELTENHAM
            "100120399951",  # FARROW & BALL, 15-17 SUFFOLK ROAD, CHELTENHAM
        ]:
            return None

        if record.housepostcode in [
            # split
            "GL50 3RB",
            "GL52 2ES",
            "GL52 6RN",
            "GL53 0HL",
            "GL50 2RF",
        ]:
            return None

        return super().address_record_to_dict(record)

    # quick fix to show maps for Halarose records that have a valid UPRN in the PollingVenueUPRN field
    def get_station_point(self, record):
        uprn = record.pollingvenueuprn.strip().lstrip("0")
        try:
            ab_rec = Address.objects.get(uprn=uprn)
            return ab_rec.location
        except ObjectDoesNotExist:
            return super().get_station_point(record)
