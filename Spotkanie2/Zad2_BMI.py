try:
    weight = float(input("Podaj swoją wagę (kg): "))
    height = float(input("Podaj swój wzrost (cm): "))
    BMI = weight / (height/100)**2
    print(round(BMI, 2))
except:
    print("Wprowadzone dane sa nieprawidolwe, podaj liczbe. Ewnetualne ulami oddziel kropka")