from addressbase.models import Address
from data_importers.management.commands import BaseHalaroseCsvImporter
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseHalaroseCsvImporter):
    council_id = "CHO"
    addresses_name = "2024-05-02/2024-02-26T15:25:45.636629/Eros_SQL_Output017.csv"
    stations_name = "2024-05-02/2024-02-26T15:25:45.636629/Eros_SQL_Output017.csv"
    elections = ["2024-05-02"]

    def station_record_to_dict(self, record):
        # TEMPORARY MOBILE STATION, WHITE HORSE CAR PARK, RAWLINSON LANE, HEATH CHARNOCK, CHORLEY, LANCS PR6 9LJ
        if record.pollingstationnumber == "35":
            record = record._replace(pollingstationpostcode="PR6 9JS")

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if uprn in [
            "100010387618",  # MILLSTONE HOUSE, THE GREEN, ECCLESTON, CHORLEY
        ]:
            return None

        if record.housepostcode in [
            # split
            "PR7 2QL",
            "PR6 0HT",
            # suspect
            "PR26 9HE",
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
