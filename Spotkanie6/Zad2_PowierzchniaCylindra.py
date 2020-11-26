import math

r = float(input("Wprowadz promien: "))
H = float(input("Wprowadz wysokosc: "))

Pp = (math.pi * r**2).__round__(2)
Pb = (2 * math.pi * r).__round__(2)
Pc = (2*Pp+Pb).__round__(2)
V = (Pp * H).__round__(2)
print(" Pp = {}\n Pb = {}\n Pc = {}\n V = {}".format(Pp, Pb, Pc, V))