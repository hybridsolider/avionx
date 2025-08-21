import csv
import sqlite3

class Waypoint:
    def __init__(self, nav_data_file, id: str, latitude, longitude, is_custom_wpt:bool=False):
        if is_custom_wpt == False:
            self.nav_data_file = nav_data_file
            self.identifier = id.upper()
            self.matches = []
        else:
            self.identifier = id.upper()
            self.latitude = latitude
            self.longitude = longitude
            

      
        with open(nav_data_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["ident"].upper() == self.identifier:
                    self.matches.append(row)

  
        if self.matches:
            self.data = self.matches[0]
        else:
            self.data = None

       
        if self.data:
            self.name = self.data.get("name")
            self.type = self.data.get("type")
            self.frequency = self.data.get("frequency_khz")
            self.latitude = self.data.get("latitude_deg")
            self.longitude = self.data.get("longitude_deg")
            self.country_code = self.data.get("iso_country")
        else:
            self.name = self.type = self.frequency = self.latitude = self.longitude = self.country_code = None

    def all_matches(self):

        return self.matches
