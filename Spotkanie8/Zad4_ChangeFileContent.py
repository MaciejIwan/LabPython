from Spotkanie8.Zad3_listToFile import write
write() # Uruchamia zadanie3 aby jakby plik Zad3 nie było wcześniej uruchomione /// Tworzy .txt

content = []
with open("Zad3_Output.txt", "r") as f:
    for line in f:
        content.extend(line.split())

content[1] = "klasa"


with open('Zad3_Output.txt', 'w') as file:
    file.write(str(content))
