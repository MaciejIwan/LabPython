slowa = (
    "Marcin",
    "Daniel",
    "Bruno",
    "Eustachy",
    "Anastazy",
    "Gniewomir",
    "Błażej",
    "Alan",
    "Ireneusz",
    "Marcel",
    "Karol",
    "Damian",
    "Albert",
    "Jan",
    "Marcel",)

with open('pietnascie.txt', 'w') as open_file:
    for k in slowa:
        open_file.write(k + '\n')

with open('pietnascie.txt', 'r') as open_file:
    text = open_file.readlines()
    size = len(text)
    print("Plik zawiera {0} wierszy".format(size))


