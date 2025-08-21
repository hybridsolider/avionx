import csv

def get_waypoint_info(identifier: str, country: str = None):
    with open("navaids.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["ident"].upper() == identifier.upper():
                if country and row["iso_country"] != country:
                    continue
                print(f"Identifier: {row['ident']}")
                print(f"Name: {row['name']}")
                print(f"Type: {row['type']}")
                print(f"Frequency: {row['frequency_khz']}")
                print(f"Latitude: {row['latitude_deg']}")
                print(f"Longitude: {row['longitude_deg']}")
                print(f"Country: {row['iso_country']}")
                return
    print(f"No waypoint found for {identifier} in {country or 'any country'}")

# Example: LDZ VOR in Poland
get_waypoint_info("LDZ", "PL")
