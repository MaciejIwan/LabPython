imiona = []
for x in range(1,5):
    imiona.append(input("Podaj Imie {} uzywtkonika: ".format(x)))

for element in imiona:
    print("Witaj uzytkowniku {}, jak Ci minął dzień?".format(element))





print("Pierwszy sposob: \n")
for x in range(4):
    t = input("Podaj cokolwiek")
    print("x: ", x, "t: ",t)

print("Drugi sposob: \n")
for x in range(34, 40):
    print("x: ", x)

print("Trzeci sposob: \n")
for y in range(10, 20, 2):
    print(y)

