import math

for x in range(5):
    y = input("Wprowadz liczbe stopni: ")
    if y in ['Q', 'q']:
        exit()
    try:
        t = math.radians(int(y))
        print(t)
    except:
        print("i mamy klopot, sprobuj ponownie")
