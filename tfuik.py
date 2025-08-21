import math

def kurs_z_A_do_C(xA, yA, xC, yC):
    delta_x = xC - xA
    delta_y = yC - yA

    # przypadek, gdy punkty pokrywają się
    if delta_x == 0 and delta_y == 0:
        return None  # kurs nieokreślony

    # przypadek dzielenia przez zero (delta_y == 0)
    if delta_y == 0:
        if delta_x > 0:
            return 90.0
        else:
            return 270.0

    # oblicz kąt w stopniach (funkcja atan zwraca w radianach)
    theta = math.degrees(math.atan(delta_x / delta_y))

    # korekta kąta wg ćwiartki
    if delta_y > 0 and delta_x >= 0:
        kurs = theta
    elif delta_y > 0 and delta_x < 0:
        kurs = theta + 360
    else:  # delta_y < 0
        kurs = theta + 180

    # upewnij się, że kurs jest w [0, 360)
    kurs %= 360

    return kurs

# Przykład użycia:
xA, yA = 0, 0
xC, yC = 1, 1

kurs = kurs_z_A_do_C(xA, yA, xC, yC)
if kurs is not None:
    print(f"Kurs z A do C: {kurs:.2f}°")
else:
    print("Punkty A i C pokrywają się, kurs nieokreślony.")
