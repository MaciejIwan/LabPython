from math import sqrt,pi
import os
def userinput():
    obwod = [0,0,0]
    T1 = input("Podaj boki 1 trojkata odzielone spacja: ").split()
    obwod[0] = Calcobwod(float(T1[0]),float(T1[1]),float(T1[2]))
    T2 = input("Podaj boki 2 trojkata odzielone spacja: ").split()
    obwod[1] = Calcobwod(float(T2[0]), float(T2[1]), float(T2[2]))
    T3 = input("Podaj boki 3 trojkata odzielone spacja: ").split()
    obwod[2] = Calcobwod(float(T3[0]), float(T3[1]), float(T3[2]))
    return max(obwod)

def Calcobwod(bok,bok2,bok3,aktualny=0):
    aktualny = bok + bok2 + bok3
    return aktualny

def obliczenieOkregow(bok):
    p_kwkw = bok ** 2
    d_kw = bok * sqrt(2)

    r = bok / 2
    poleWpisanego = (pi * r ** 2).__round__(2)
    obwodWpisanego = (2 * pi * r).__round__(2)
    print("Pole wpisanego okręgu: {}, jego obwod: {}".format(poleWpisanego, obwodWpisanego))

    r2 = d_kw / 2
    poleOpisanego = (pi * r2 ** 2).__round__(2)
    obwodOpisanego = (2 * pi * r2).__round__(2)
    print("Pole opisanego okręgu: {}, jego obwod: {}".format(poleOpisanego, obwodOpisanego))


clear = lambda: os.system('cls')
x = userinput()


print("\n\n\n\n\n")
if x < 150: print("Pole poniżej 150! bo najwiekszy z nich ma pole: {}".format(x))
if x > 150: print("Pole powyzej 150! bo najwiekszy z nich ma pole: {}".format(x))

obliczenieOkregow(x)



