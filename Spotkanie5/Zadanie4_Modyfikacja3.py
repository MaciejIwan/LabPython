def Obliczam(pensja,podatek,ubezpieczenie,ppk):
    netto = pensja*(1-podatek/100)*(1-ubezpieczenie/100)*(1-ppk/100)
    return netto

while True:
    try:
        p = float(input("Twoja pensja: "))
        pod = float(input("Stawka podatku w %: "))
        u = float(input("Skladki na ubezpieczenie zdrowotne w %: "))
        ppk = float(input("stawka ppk w procentach: "))
        print("Do Twojej kieszeni trafi: {}".format(Obliczam(p,pod,u,ppk)))

        break
    except:
        print("Sprobuj ponownie\n")
