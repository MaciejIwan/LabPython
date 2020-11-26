import math as m

while True:
    try:
        a = float(input("Podaj kat aby obliczbyc luk: "))
        if a > 360:
            print("Twój łuk jest większy niż pełne koło, zdaje sie że to nie powinno tak wyglądać")
            continue
        r = float(input("Podaj promien kola: "))
        l = (m.radians(a) * r).__round__(2)
        p = ((m.radians(a)/2) * r**2).__round__(2)
        print("Długośc łuku: {}\nZakreslone pole: {}".format(l,p))
        break
    except:
        print("Sprobuj ponownie")
