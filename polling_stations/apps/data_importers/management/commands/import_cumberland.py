from addressbase.models import Address
from data_importers.management.commands import BaseHalaroseCsvImporter
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseHalaroseCsvImporter):
    council_id = "CBD"
    addresses_name = "2024-05-02/2024-04-17T07:02:46.229815/Eros_SQL_Output001.csv"
    stations_name = "2024-05-02/2024-04-17T07:02:46.229815/Eros_SQL_Output001.csv"
    elections = ["2024-05-02"]

    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if uprn in [
            "10008699323",  # HOWDALE, KIRKCAMBECK, BRAMPTON
            "10008692803",  # THE LYNES, ROWELTOWN, CARLISLE
            "10008692455",  # STOTT FOOT COTTAGE, LONGTOWN, CARLISLE
            "10008685504",  # CHAPEL TOWN, EASTON, LONGTOWN, CARLISLE
            "10009462560",  # WALLHOLME, LOW ROW, BRAMPTON
            "10008705150",  # GELT BRIDGE FARM, BRAMPTON
            "10008691849",  # GELT MILL HOUSE, CASTLE CARROCK, BRAMPTON
            "100110687222",  # MOORVALE, SANDY LANE, BROADWATH, HEADS NOOK, BRAMPTON
            "10008698916",  # BERRYMOOR, HEADS NOOK, BRAMPTON
            "10008693117",  # THE BARN, NEWBY CROSS, CARLISLE
            "10008710861",  # ANNEX AT THE BARN NEWBY CROSS VILLAGE, NEWBY CROSS
            "100110220886",  # 8A PENRITH ROAD, KESWICK
            "100110220887",  # 8 PENRITH ROAD, KESWICK
            "100110683374",  # LINGHOLM, PORTINSCALE, KESWICK
            "10000899045",  # STABLE COTTAGE, STEEL GREEN, MILLOM
            "10000897322",  # STEEL GREEN HOUSE, STEEL GREEN, MILLOM
            "10000906979",  # FLAT AT HERDWICKS STEEL GREEN, MILLOM
            "10000898440",  # LOWSIDE BARN, EGREMONT
            "100110308201",  # 195 FRIZINGTON ROAD, FRIZINGTON
            "10094282417",  # 37 GRAYLING WAY, WORKINGTON
            "10094282418",  # 39 GRAYLING WAY, WORKINGTON
            "10094282419",  # 41 GRAYLING WAY, WORKINGTON
            "10094286569",  # FLAT 29 STATION ROAD, WORKINGTON
            "100110222536",  # 35 EAGLESFIELD STREET, MARYPORT
            "10008822382",  # HOLIDAY LET, SUNSET VIEW AND MEADOW LODGE PASTURE FARM WESTNEWTON ROAD, ASPATRIA
            "10008818804",  # SPRING LEA, KIRKBRIDE, WIGTON
            "10012987752",  # LAUREL HOUSE, KIRKBRIDE, WIGTON
            "10008818771",  # OLD STATION HOUSE, KIRKBRIDE, WIGTON
            "10014286700",  # BEECHINGS CUT, KIRKBRIDE, WIGTON
            "10012990290",  # SEPTEMBER HOUSE, WHITRIGGLEES, KIRKBRIDE, WIGTON
            "100110292402",  # 2A NORFOLK STREET, CARLISLE
            "10008694620",  # 1 ORCHARD LEA, CARLISLE
            "10008684694",  # 2 ORCHARD LEA, CARLISLE
            "10008683403",  # HARRABY SCHOOL HOUSE, EDGEHILL ROAD, CARLISLE
            "100110231540",  # 34 EDINBURGH AVENUE, WORKINGTON
            "10000899104",  # 1 LONSDALE HOUSE, NORTH SHORE, WHITEHAVEN
        ]:
            return None

        if record.housepostcode in [
            # splits
            "CA15 7RL",
            "CA22 2TD",
            "CA25 5LN",
            "CA2 7LS",
            "CA2 4RE",
            "CA25 5JE",
            "CA7 0EG",
            "CA26 3RU",
            "CA28 6TU",
            "CA5 6JS",
            "CA6 4LF",
            "CA25 5LH",
            "LA19 5XT",
            # looks wrong
            "CA12 4GN",
            "CA12 4TP",
            "CA26 3RE",
            "CA7 5HX",
        ]:
            return None

        return super().address_record_to_dict(record)

    def station_record_to_dict(self, record):
        # Postcode in wrong column: Watson Hall, Castle Carrock, Brampton, CA8 9LU
        if record.pollingstationnumber == "123":
            record = record._replace(pollingstationpostcode="CA8 9LU")

        # Postcode correction for: Portable Cabin, Borrowdale Road, Carlisle, CA2 6RD
        if record.pollingstationnumber == "180":
            record = record._replace(pollingstationpostcode="")

        # Postcode correction for: Low Moor Evangelical Church, Low Moor Road, Wigton, Cumbria, CA7 8QP
        if record.pollingstationnumber == "96":
            record = record._replace(pollingstationpostcode="")

        # Postcode correction for: Welfare Hall, Little Broughton, Cockermouth, Cumbria, CA13 0ZX
        if record.pollingstationnumber == "21":
            record = record._replace(pollingstationpostcode="")

        return super().station_record_to_dict(record)

    # quick fix to show maps for Halarose records that have a valid UPRN in the PollingVenueUPRN field
    def get_station_point(self, record):
        uprn = record.pollingvenueuprn.strip().lstrip("0")
        try:
            ab_rec = Address.objects.get(uprn=uprn)
            return ab_rec.location
        except ObjectDoesNotExist:
            return super().get_station_point(record)
