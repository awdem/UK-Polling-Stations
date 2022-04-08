from django.utils.text import slugify

from data_importers.github_importer import BaseGitHubImporter


class Command(BaseGitHubImporter):

    srid = 4326
    districts_srid = 4326
    council_id = "DND"
    elections = ["2022-05-05"]
    scraper_name = "wdiv-scrapers/DC-PollingStations-Dundee"
    geom_type = "geojson"

    def district_record_to_dict(self, record):
        poly = self.extract_geometry(record, self.geom_type, self.get_srid("districts"))

        return {
            "internal_council_id": record["POLLING_DISTRICT"],
            "name": record["POLLING_DISTRICT"],
            "area": poly,
        }

    def station_record_to_dict(self, record):
        location = self.extract_geometry(
            record, self.geom_type, self.get_srid("stations")
        )
        return {
            "internal_council_id": f'{slugify(record["WARD"])}-{record["POLLINGSTATIONID"]}',
            "address": record["PS_ADDRESS"],
            "postcode": "",
            "location": location,
            "polling_district_id": record["POLLINGDISTRICTREFERENCE"],
        }
