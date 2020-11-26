while True:
    try:
        liczba = int(input("Podaj liczbe od 1 do 10: "))
        silnia = 1
        for x in range(liczba):
            silnia = silnia * (x+1)
        print("Silnia {0} wynosi {1}".format(liczba,silnia))
        break
    except ValueError:
        print("Wprowadzane znaki nie są liczbami")


while True:
    try:
        liczba = int(input("Podaj liczbe od 1 do 10: "))
        silnia = 1
        x = 1
        while True:
            silnia = silnia * x
            x += 1
            if x > liczba:
                break
        print("Silnia {0} wynosi {1}".format(liczba, silnia))
        break
    except:
        print("Coś poszło nie tak")