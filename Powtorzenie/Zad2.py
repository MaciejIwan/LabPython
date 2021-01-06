def podzielnosc(number):
    # przedzial 0 24 tra
    suma = 0
    for x in range(number[0],number[1]+1):
        if x % 6 == 0 and x % 4 == 0:
            print("Liczba {} jest podzielna przez 4 i 6".format(x))
            suma += x
    print("\nSuma liczb podzielnych przez 4 i 6 w zakresie od {0} do {1} wynosi: {2}".format(number[0], number[1], suma))

#Przedzial funkcji traktujemy jako zamknięty
przedzial = (0, 24)
podzielnosc(przedzial)

