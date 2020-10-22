try:
    x = []
    x.append(input("Podaj pierwsza wartosc: "))
    x.append(input("Podaj drugą wartosc: "))
    x.append(input("Podaj trzecią wartosc: "))
    x.sort()
    print(x)
except:
    print("Coś poszło nie tak")