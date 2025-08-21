import math
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def stopnie_na_radiany(deg):
    return deg * math.pi / 180

def radiany_na_stopnie(rad):
    deg = rad * 180 / math.pi
    return deg % 360

def wspolrzedne(r, radial_deg):
    theta = stopnie_na_radiany(radial_deg)
    x = r * math.sin(theta)
    y = r * math.cos(theta)
    return x, y

def dystans(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def kurs_od_A_do_C(xA, yA, xC, yC):
    dx = xC - xA
    dy = yC - yA
    angle_rad = math.atan2(dx, dy)  # atan2(x, y) żeby 0° było na północ
    return radiany_na_stopnie(angle_rad)

def rnav_dme(xA, yA, xC, yC, radial_C_deg):
    # Kurs odwrotny do radialu waypointa (CRS)
    CRS_deg = (radial_C_deg + 180) % 360
    theta_CRS = stopnie_na_radiany(CRS_deg)
    dx_CRS = math.sin(theta_CRS)
    dy_CRS = math.cos(theta_CRS)

    # Wektor z waypointa do samolotu
    vx = xA - xC
    vy = yA - yC

    # Rzut wektora na linię CRS (odległość RNAV DME)
    return abs(vx * dx_CRS + vy * dy_CRS)

def main():
    clear_console()
    print("Podaj dane punktu A (samolot):")
    radial_A = float(input("Radial z VOR do punktu A (stopnie): "))
    distance_A = float(input("Dystans z VOR do punktu A (NM): "))

    print("\nPodaj dane punktu C (waypoint):")
    radial_C = float(input("Radial z VOR do punktu C (stopnie): "))
    distance_C = float(input("Dystans z VOR do punktu C (NM): "))

    xA, yA = wspolrzedne(distance_A, radial_A)
    xC, yC = wspolrzedne(distance_C, radial_C)

    dist_AC = dystans(xA, yA, xC, yC)
    kurs = kurs_od_A_do_C(xA, yA, xC, yC)
    dme = rnav_dme(xA, yA, xC, yC, radial_C)



    print(f"Kurs z A do C: {kurs:.2f}° (UWAGA! KURS NIE UWZGLĘDNIA WIATRU!)")
    print(f"RNAV DME (odległość na osi CRS): {dme:.2f} NM")

if __name__ == "__main__":
    main()
