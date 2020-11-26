def mnozenie(liczba,mnoznik,drugimnoznik,wynik=0):
    for x in range(mnoznik):
        wynik += liczba
    wynik2 = 0
    for x in range(drugimnoznik):
        wynik2 += wynik
    return wynik2



while True:
    try:
        x = int(input("Liczbe ktora bedziesz mnozyc: "))
        y = int(input("Przez co bedziesz ją mnożyć: "))
        z = int(input("Druga przez która będziesz mnożyć: "))
        print("Wynik: {}".format(mnozenie(x, y,z)))
        break
    except:
        print("Sprobuj ponownie")


