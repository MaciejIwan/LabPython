import Spotkanie8.Zad1_Imie_Nazwisko_do_pliku

content = []
with open("Zad1_Output.txt", "r") as f:
    for line in f:
        content.extend(line.split())

print(content[1])