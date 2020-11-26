def justmagic(x,y,suma=0):
    for i in range(x,y+1):
        if (i % 3) == 0 or (i % 6) == 0:
            suma += i
    return suma


while True:
    try:
        dolny = int(input("podaj dolny zakres: "))
        gorny = int(input("podaj gorny zakres: "))
        print(justmagic(dolny,gorny))
        break
    except:
        print("Sprobuj ponownie\n")