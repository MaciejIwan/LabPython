import math as m

while True:
    try:
        a = float(input("Podaj kat aby obliczbyc luk: "))
        if a > 360:
            print("Twój łuk jest większy niż pełne koło, zdaje sie że to nie powinno tak wyglądać")
            continue
        r = float(input("Podaj promien kola: "))
        l = m.radians(a)*r
        print("Wynik: {}".format(l))
        break
    except:
        print("Sprobuj ponownie")
