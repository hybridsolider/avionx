import csv
import sqlite3



nav_data_file = "data/map/navdata.csv"
airport_data_file = "data/map/airports.csv"
airport_freq_file = "data/map/airport_freqs.csv"

class Waypoint:
    def __init__(self, id: str, latitude, longitude, is_custom_wpt:bool=False):
        global nav_data_file
        
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


class Airport_frequency:
    def __init__(self, id: str):
        global airport_freq_file
        
        self.airport_freq_file = airport_freq_file
        self.identifier = id.upper()
        self.matches = []
        self.frequency = {}

        with open(airport_freq_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["airport_ident"].upper() == self.identifier:
                    self.matches.append(row)
                    
        for match in self.matches:
            t = match["type"]  # this is the "main key"
            
            self.frequency[t] = {
                "airport_ident": match.get("airport_ident"),
                "type": match.get("type"),
                "description": match.get("description"),
                "frequency_mhz": match.get("frequency_mhz"),
            }



class Airport:
    
    def __init__(self, id: str):
        global airport_data_file
        self.airport_data_file = airport_data_file
        self.identifier = id.upper()
        self.matches = []


        with open(airport_data_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["ident"].upper() == self.identifier:
                    self.matches.append(row)
                    
        
        
        if self.matches:
            self.data = self.matches[0]
        else:
            self.data = None
            
        if self.data:
            self.identifier = self.data.get("ident")
            self.name = self.data.get("name")
            self.type = self.data.get("type")
            self.latitude = self.data.get("latitude_deg")
            self.longitude = self.data.get("longitude_deg")
            self.elevation_ft = self.data.get("elevation_ft")
            self.municipality = self.data.get("municipality")
            self.country_code = self.data.get("iso_country")
            self.frequencies = Airport_frequency(self.identifier).frequency
            



epwa = Airport("epwa")

print(epwa.frequencies)