import random
a_powitanie = "Uważaj gierka zweryfikuje Twoje szczęscie, \nAby wygrać wpisuj liczbe od 0 do 20 w kazddej rundzie wygrywa tylko jeden numer\n"
a_zwyciestwo = "\nHURRRAAAAA Rozbiłeś bank!"
a_proba = ["Podana liczba jest zbyt mała, spróbuj ponownie", "Podana liczba jest za duża, spróbuj ponownie"]
a_zlaWartosc = "Podana wartosc nie jest obslugiwana, sprobuj ponownie"

print(a_powitanie)
x = random.randint(1, 20)
print(x)

while True:
    Strzal = input('Wpisz liczbę: ')
    try:
        Strzal = int(Strzal)
    except:
        print(a_zlaWartosc)
        continue
    if x == Strzal:
        break
    if Strzal > x: result = 1
    else: result = 0
    print(a_proba[result])
print(a_zwyciestwo)
