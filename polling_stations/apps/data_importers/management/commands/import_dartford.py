from data_importers.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "DAR"
    addresses_name = "2024-07-04/2024-06-05T15:57:04.146018/Eros_SQL_Output003.csv"
    stations_name = "2024-07-04/2024-06-05T15:57:04.146018/Eros_SQL_Output003.csv"
    elections = ["2024-07-04"]

    def station_record_to_dict(self, record):
        # Below stations are throwing a warning about different postcode in the addressbase, but council requested to keep them.
        # Wentworth Primary School, Entrance via James Road, Wentworth Drive, Dartford, Kent, DA1 3NF
        # Temple Hill Community Centre, Temple Hill Square, Dartford, Kent, DA1 5HX
        # The Gateway Primary Academy (SHO1), Milestone Road, Dartford, Kent, DA2 6PL
        # St Albans Church, St Albans Road, Dartford, Kent, DA1 1TE
        # Oakfield Primary Academy (PRI5), Oakfield Lane, Dartford, Kent, DA1 2SW

        return super().station_record_to_dict(record)
