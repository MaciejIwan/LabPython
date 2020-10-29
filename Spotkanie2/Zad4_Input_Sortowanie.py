try:
    x = []
    x.append(input("Podaj pierwsza wartosc: "))
    x.append(input("Podaj drugą wartosc: "))
    x.append(input("Podaj trzecią wartosc: "))
    x.sort()
    for elements in x:
        print(elements)
except:
    print("Coś poszło nie tak")