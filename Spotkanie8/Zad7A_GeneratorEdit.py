import random
elementy = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", "!@#$%^&*()"]
password = ""

for x in range(8):
    if x == 0:
        password = password + random.choice(elementy[0])
    elif x == 1:
        password = password + random.choice(elementy[1])
    elif x == 2:
        password = password + random.choice(elementy[2])
    elif x == 3:
        password = password + random.choice(elementy[3])
    else:
        r_int = random.randint(0,3) #Losowanie typu znaku
        password = password + random.choice(elementy[r_int]) #losowy znak losowego typu

final_password = list(password)
random.shuffle(final_password)
with open('haslo.txt', 'w') as of:
    for element in final_password:
        of.write(element)
        of.write(" ")
