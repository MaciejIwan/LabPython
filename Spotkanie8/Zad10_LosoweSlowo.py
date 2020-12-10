import random
with open('sowpods.txt', 'r') as f1:
    with open('Losowanie.txt', 'w') as f2:
        f2.write(random.choice(f1.readlines()))