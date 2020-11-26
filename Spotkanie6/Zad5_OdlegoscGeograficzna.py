import math


def distance_between_coords(lat1, lat2, lon1, lon2):
    r = 6371
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)

    dlat = lat1 - lat2
    dlon = lon1 - lon2
    return 2*r*math.asin(math.sqrt(math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2))


lat1 = float(input("Podaj 1. szerokość geograficzną: "))
lon1 = float(input("Podaj 1. długość geograficzną: "))
lat2 = float(input("Podaj 2. szerokość geograficzną: "))
lon2 = float(input("Podaj 2. długość geograficzną: "))
print("odległość wynosi: ", distance_between_coords(lat1, lat2, lon1, lon2).__round__(3), "km")
