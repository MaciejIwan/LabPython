import time

def myFunc(powtorzenia):
    for x in range(1,powtorzenia+1):
        if not x%3 and not x%4: print("Liczba {} dzieli sie przez 3 oraz 4".format(x))
        elif not x%3: print("Liczba {} dzieli sie przez przez 3".format(x))
        elif not x%4: print("Liczba {} dzieli sie przez przez 4".format(x))
        else: print("Liczba {} nie jest podzielna przez 3 ani 4".format(x))



while True:
    try:
        x = int(input("Ile razy chcesz wykonać prgoram: "))
        start = time.time()
        myFunc(x)
        stop = time.time()
        print("{} sekundy".format(stop-start))
        break
    except:
        print("Sprobuj ponownie, podaj liczbe calkowita")



# ==================================================================================
# ==================================================================================
print("\n\n\nDruga Wersja\n\n")
# ==================================================================================

def check_number(num):
    if not num % 3 and not x % 4: return"Liczba {} dzieli sie przez 3 oraz 4".format(num)
    elif not num % 3: return"Liczba {} dzieli sie przez przez 3".format(num)
    elif not num % 4:return"Liczba {} dzieli sie przez przez 4".format(num)
    else: return"Liczba {} nie jest podzielna przez 3 ani 4".format(num)


while True:
    try:
        x = int(input("Ile razy chcesz wykonać prgoram: "))
        start = time.time()
        for i in range(x):
            print(check_number(i+1))
        stop = time.time()
        print("{} sekundy".format(stop-start))
        break
    except:
        print("Sprobuj ponownie, podaj liczbe calkowita")
