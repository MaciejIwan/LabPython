def Obliczam(pensja):
    if pensja < 1000:
        print("Zgłoś się po pomoc możliwe że jesteś wykorzystywany")
    if pensja in range(1000,3601):
        podatek = 0.12
        ubezpieczenie = 0.10
        ppk = 0.02
    if pensja >= 3601:
        podatek = 0.14
        ubezpieczenie = 0.12
        ppk = 0.03
    netto = pensja*(1-podatek)*(1-ubezpieczenie)*(1-ppk)
    return netto

while True:
    try:
        print("Do Twojej kieszeni wpada: {} PLN netto".format(Obliczam(float(input("Podaj wartosc swojej pensji brutto")))))
        break
    except:
        print("Sprobuj ponownie\n")
