# def ola():
#     print("Funkcja ola")
#     return 1
#
# def marcin():
#     print("1 w fukncji Marcin")
#     x = "Wartosc X"
#     print("2 w funkcji Marcin")
#     return 'OLA'
#
#
#
# odp = "Startowa wartość odpowiedzi"
# print("0")
# print(odp)
# print("0.5")
# marcin()
# print("3")
# odp = marcin()
# print("4")
# print(odp)
# print("5")


def pracownik(x):
    if x < 10: print("X jest mniejsze niz 10")
    if x > 10: print("X jest wieksze niz 10")
    if x == 10: print("X jest rowne 10")


for i in range(4):
    print(i)
    numer = int(input("Podaj liczbe"))
    pracownik(numer)



pracownik(10)



