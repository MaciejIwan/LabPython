import random

slowa = ["mama", "tata", "wuj", "corka"]
losowe = slowa[random.randint(0, 4)]
#print(losowe)
new_word = list(losowe)
#print(new_word)
random.shuffle(new_word)
print(new_word)

User_word = ''
while User_word != losowe:
    User_word = input("Ułóż słowo z powyższych liter ")
    if User_word == 'q' or User_word == 'Q': #exit program
        print("Przerwałes program")
        exit()
print("Eurreka wygrałeś")
