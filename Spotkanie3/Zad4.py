text = input("Podaj imiona oddzielone spacja: ")
text.replace(',', ' ')
imiona = text.split()

for element in imiona:
    print("Witaj uzytkowniku {}, jak Ci minął dzień?".format(element))