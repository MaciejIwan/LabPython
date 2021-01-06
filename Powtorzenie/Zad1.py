from random import shuffle, randint


def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

words = ["uczelnia", "katedra", "instytut", "aula", "pracownia", "laboratorium"]
chosen = words[randint(0, 5)]
print(shuffle_word(chosen))
word = ''
while word != chosen:
    word = input("Pewne słowo zostało pomieszane, ułóż słowo z powyższych liter: ")
    if word == 'q' or word == 'Q':
        print("Szkoda, że się poddałeś")
        quit()
print("Brawo! Udało ci się")
