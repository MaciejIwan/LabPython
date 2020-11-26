imie = input("Podaj Imie: ")
nazwisko = input("Podaj Nazwisko: ")
with open('Zad1_Output.txt', 'w') as open_file:
    open_file.write(imie + ' ' + nazwisko)