text = input("Podaj imiona oddzielone spacja: ")
imiona = text.split()

for element in imiona:
    print("Witaj uzytkowniku {}, jak Ci minął dzień?".format(element))