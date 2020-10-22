try:
    print("Podaj 3 boki trojkata")
    a = float(input("bok a: "))
    b = float(input("bok b: "))
    c = float(input("bok c: "))
    if a+b>c and a+c>b and b+c>a:
        print("Mozliwe jest zbudowanie trojkata o bokach",a,b,c)
    else:
        print("Taki trojkat nie moze istniec")
except:
    print("Podana wartosc nie jest liczba")

