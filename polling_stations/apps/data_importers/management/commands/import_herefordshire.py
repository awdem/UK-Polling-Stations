from addressbase.models import Address
from data_importers.management.commands import BaseHalaroseCsvImporter
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseHalaroseCsvImporter):
    council_id = "HEF"
    addresses_name = "2024-05-02/2024-02-28T13:29:48.569126/Democracy Club polling station export.csv"
    stations_name = "2024-05-02/2024-02-28T13:29:48.569126/Democracy Club polling station export.csv"
    elections = ["2024-05-02"]

    # Following warning checked and no need for correction:
    # WARNING: Polling station Richards Castle Village Hall (15-richards-castle-village-hall) is in Shropshire Council (SHR)
    def address_record_to_dict(self, record):
        uprn = record.uprn.strip().lstrip("0")

        if uprn in [
            "10009576751",  # FARMHOUSE HILL OAK FARM C1136 FROM C1135 TO HILL OAK FARM, BISHOPS FROME
            "10009563043",  # MESSUAGE COTTAGE, THE GOGGIN, RICHARDS CASTLE, LUDLOW
            "10022775386",  # CAMP HILL COTTAGE, LOWER LYE, AYMESTREY, LEOMINSTER
            "10009580590",  # HUNDRED HOUSE, THE HUNDRED, MIDDLETON ON THE HILL, LEOMINSTER
            "10022783867",  # OLD HILL BARN, EYTON, LEOMINSTER
            "10009580620",  # LAMMAS COTTAGE, LOWER WOODHOUSE, SHOBDON, LEOMINSTER
            "10093121165",  # THE DAIRY AT THE GROVE THE GROVE NOKE LANE, PEMBRIDGE
            "10022782220",  # THE CARAVAN PORTLEY BUILDINGS LUDLOW ROAD, LEOMINSTER
            "10009556889",  # CANTERBURY COTTAGE, SHOBDON, LEOMINSTER
            "10008146492",  # YEW TREE COTTAGE, WOONTON, HEREFORD
            "10009570376",  # VESTRY, KINGTON
            "10009576148",  # CAT & FIDDLE COTTAGE, WORMBRIDGE, HEREFORD
            "10009568749",  # THE OLD LANDS, PONTRILAS, HEREFORD
            "10009569115",  # THE RED BARN, PENCRAIG, ROSS-ON-WYE
            "200002634830",  # HAZEL COTTAGE, BAILEY LANE END, ROSS-ON-WYE
            "10009572783",  # NOCELYON, CASTLE END FARM, LEA, ROSS-ON-WYE
            "10009564876",  # BIRDS NEST, LEA, ROSS-ON-WYE
            "10009555309",  # ASHTREE COTTAGE, HOW CAPLE, HEREFORD
            "10009571795",  # YEW TREE COTTAGE, HOW CAPLE, HEREFORD
            "200002633179",  # 2 KIMBERROWS, FALCON LANE, LEDBURY
            "200002633178",  # 1 KIMBERROWS, FALCON LANE, LEDBURY
            "10009565510",  # RHEA COTTAGE, ACTON BEAUCHAMP, WORCESTER
            "10094167692",  # 35 TOWER COURT, SALTMARSHE CASTLE PARK, TEDSTONE WAFRE, BROMYARD
            "10094168126",  # 34 TOWER COURT, SALTMARSHE CASTLE PARK, TEDSTONE WAFRE, BROMYARD
            "10094168124",  # 32 TOWER COURT AT SALTMARSHE CASTLE PARK SALTMARSH CASTLE ACCESS, TEDSTONE WAFRE
            "10094168123",  # 31 TOWER COURT, SALTMARSHE CASTLE PARK, TEDSTONE WAFRE, BROMYARD
            "10009568842",  # THE OLD SCHOOL, TEDSTONE WAFRE, BROMYARD
            "10007369285",  # MONTREL FARM, HATFIELD, LEOMINSTER
            "10009566778",  # STEPHENS COTTAGE, DOCKLOW, LEOMINSTER
            "10007369318",  # MAWKINGFIELD COTTAGE, DOCKLOW, LEOMINSTER
            "10023976028",  # CARAVAN AT CASTLEFIELD ADJACENT WHEELBARROW STOKE PRIOR LANE, LEOMINSTER
            "10023977579",  # WHITESTONES FARM, THE GOGGIN, RICHARDS CASTLE, LUDLOW
            "10009571148",  # WILLOW COTTAGE, THE GOGGIN, RICHARDS CASTLE, LUDLOW
            "10009562176",  # LODGE FARM, WALTERSTONE, HEREFORD
            "10093121067",  # THATCH COTTAGE, WHITFIELD, HEREFORD
            "10009559827",  # GRITHILL LODGE, WHITFIELD, HEREFORD
            "10009556830",  # CALDICOTT FARM, HOLME LACY, HEREFORD
            "200002596827",  # 15 ROSS ROAD, HEREFORD
            "200002596828",  # 35 ROSS ROAD, HEREFORD
            "10022781578",  # DUNROB, RIDGEHILL, HEREFORD
            "10094169418",  # POOL VIEW, ROMAN ROAD, HEREFORD
            "10009561079",  # IVY COTTAGE, BRINGSTY, WORCESTER
            "10009560952",  # HORSNETT, LINLEY GREEN ROAD, WHITBOURNE, WORCESTER
            "10009577360",  # 2 THE OLD WEIR COTTAGE A438 FROM MARSH COURT ACCESS TO KINGS ACRE ROAD, SWAINSHILL
            "10009555005",  # ABBEY COURT FARM, WIGMORE, LEOMINSTER
            "10009561940",  # LITTLE FROME MILL LINTON LANE, BROMYARD
            "10009560952",  # HORSNETT, LINLEY GREEN ROAD, WHITBOURNE, WORCESTER
            "10007360394",  # THE GROVE, NOKE LANE, PEMBRIDGE, LEOMINSTER
            "10009559954",  # HAMPTON MILL, HOPE-UNDER-DINMORE, LEOMINSTER
            "10007368198",  # HUNGRY HILL HOUSE STOKES LANE, STOKE LACY
            "10009559121",  # THE POOL, BOSBURY, LEDBURY
        ]:
            return None

        if record.housepostcode in [
            # looks wrong
            "HR6 0DS",
            "HR6 0AN",
            "WR6 5RD",
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
