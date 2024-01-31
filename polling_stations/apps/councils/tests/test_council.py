from councils.models import Council
from councils.tests.factories import CouncilFactory
from django.test import TestCase
from pollingstations.tests.factories import PollingStationFactory


class CouncilTest(TestCase):
    def setUp(self):
        nwp_council = CouncilFactory(
            **{
                "council_id": "NWP",
                "electoral_services_address": "Newport City Council\nCivic Centre\nNewport\nSouth Wales",
                "electoral_services_email": "uvote@newport.gov.uk",
                "electoral_services_phone_numbers": ["01633 656656"],
                "electoral_services_postcode": "NP20 4UR",
                "electoral_services_website": "http://www.newport.gov.uk/_dc/index.cfm?fuseaction=electoral.homepage",
                "name": "Newport Council",
                "identifiers": ["W06000022"],
            }
        )
        PollingStationFactory(council=nwp_council)
        stations_council = CouncilFactory()
        PollingStationFactory(council=stations_council)
        CouncilFactory(council_id="JKL", name="No Stations Council")

    def test_nation(self):
        newport = Council.objects.get(pk="NWP")
        self.assertEqual("Wales", newport.nation)

    def test_with_polling_stations_in_db_qs(self):
        self.assertEqual(len(Council.objects.all()), 3)
        self.assertEqual(len(Council.objects.with_polling_stations_in_db()), 2)
