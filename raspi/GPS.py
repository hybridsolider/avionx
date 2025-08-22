import csv
import sqlite3
import math

import flight_math
import settings

nav_data_file = settings.nav_data_file
airport_data_file = settings.airport_data_file
airport_freq_file = settings.airport_freq_file

class Waypoint:
    def __init__(self, id: str, latitude=None, longitude=None, is_custom_wpt:bool=False):
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
            self.magnetic_variation = self.data.get("magnetic_variation_deg")
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
            



        
    def calc_distance(lat1, lon1, lat2, lon2) -> float:
        # earth radius
        # R = 6371.0  km
        R = 3440.0 # NM
        
        #deg -> rad
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        
        #calculating Δφ Δλ
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        
        # calculating distance
        a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
        c = math.atan(math.sqrt(a))
        
        return R * c * 2


