import math

class Course_calc: 
    def calc_magnetic_correction(id:str):
        import GPS
        if len(id) == 4:
            return 0
        
        wpt = GPS.Waypoint(id)
        return wpt.magnetic_variation
    
    def calc_wind_correction_angle(wind_angle, wind_speed, CRS, TAS):
        CRS = math.radians(CRS)
        wind_angle = math.radians(wind_angle)
        WCA = math.asin((wind_speed/TAS) * math.sin(wind_angle - CRS))
        
        return round(WCA,2)
    
    def calc_course(lat1, lat2, lon1, lon2): # θ=atan2(sinΔλ⋅cosφ2​,cosφ1​⋅sinφ2​−sinφ1​⋅cosφ2​⋅cosΔλ)
        lambda1 = math.radians(lon1)
        lambda2 = math.radians(lon2)
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)

        delta_lambda = lambda2 - lambda1
        
        a = math.sin(delta_lambda) * math.cos(phi2)
        b = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(delta_lambda)
        theta = math.atan2(a, b)
        return round(math.degrees(theta))


