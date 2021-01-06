list = [1, 2, 3, 3, 3, 5]
trojka = 0
for x in list:
    if x == 3:
        trojka += 1
list.remove(1)
print("Trojka wystepuje {0} razy".format(trojka))
for x in list:
    print("{0} ".format(x), end ="")

print("\n\n\nPoniżej rozwiązanie z wykorzystaniem biblioteki array: \n\n\n")

import array
trojka = 0
my_arr = array.array("i", [1, 2, 3, 3, 3, 5])
for x in my_arr:
    if x == 3:
        trojka += 1
print("Trojka wystepuje {0} razy".format(trojka))
my_arr.remove(1)
for x in my_arr:
    print("{0} ".format(x), end ="")

