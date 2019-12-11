from django.core.management.base import BaseCommand

from django.contrib.gis.geos import Point
from pollingstations.models import PollingStation, PollingDistrict, ResidentialAddress
from councils.models import Council
from addressbase.models import Address


def update_station_point(council_id, station_id, point):
    stations = PollingStation.objects.filter(
        council_id=council_id, internal_council_id=station_id
    )
    if len(stations) == 1:
        station = stations[0]
        station.location = point
        station.save()
        print("..updated")
    else:
        print("..NOT updated")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # User issue 230
        print("updating: West Oxford Community Centre (Oxford)...")
        update_station_point(
            "E07000178", "5354", Point(-1.274921, 51.752621, srid=4326)
        )

        # User issue 238
        print("updating: YMCA - Lawnswood Branch (Leeds)...")
        update_station_point(
            "E08000035", "7664", Point(-1.595989, 53.844380, srid=4326)
        )

        # User issue 239
        print("updating: Merrion House (Leeds)...")
        stations = PollingStation.objects.filter(
            council_id="E08000035", internal_council_id="7387"
        )
        if len(stations) == 1:
            station = stations[0]
            station.postcode = "LS2 8PD"
            station.location = None
            station.save()
            print("..updated")
        else:
            print("..NOT updated")

        print("removing bad points from AddressBase")
        bad_uprns = [
            # nothing yet
        ]
        addresses = Address.objects.filter(pk__in=bad_uprns)
        for address in addresses:
            print(address.uprn)
            address.delete()
        print("..deleted")

        deleteme = [
            # nothing yet
        ]
        for council_id in deleteme:
            print("Deleting data for council %s..." % (council_id))
            # check this council exists
            c = Council.objects.get(pk=council_id)
            print(c.name)

            PollingStation.objects.filter(council=council_id).delete()
            PollingDistrict.objects.filter(council=council_id).delete()
            ResidentialAddress.objects.filter(council=council_id).delete()
            print("..deleted")

        print("..done")
