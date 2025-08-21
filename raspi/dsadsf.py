import csv

nav_data_file = "navaids.csv"


class Waypoint:
    def __init__(self, nav_data_file, identifier: str):
        self.nav_data_file = nav_data_file
        self.identifier = identifier

    def get_identifier(self):
        with open(self.nav_data_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["ident"].upper() == self.identifier.upper():
                    return row
        return None
    def get_name(self):
        waypoint = self.get_identifier(self.identifier)
        if waypoint:
            return waypoint["name"]
        return None
    def get_type(self):
        waypoint = self.get_identifier(self.identifier)
        if waypoint:
            return waypoint["type"]
        return None
    def get_frequency(self):
        waypoint = self.get_identifier(self.identifier)
        if waypoint:
            return waypoint["frequency_khz"]
        return None
    def get_latitude(self):
        waypoint = self.get_identifier(self.identifier)
        if waypoint:
            return waypoint["latitude_deg"]
        return None
    def get_longitude(self):
        waypoint = self.get_identifier(self.identifier)
        if waypoint:
            return waypoint["longitude_deg"]
        return None
    def get_country(self):
        waypoint = self.get_identifier(self.identifier)
        if waypoint:
            return waypoint["iso_country"]
        return None




