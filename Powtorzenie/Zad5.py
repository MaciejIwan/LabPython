import array
my_array = array.array('i', [1,2,3,4,5,6,7,8,9,1])
count = 0
indeks = 0
for i in my_array:
    if i == 1 and count == 1:
        my_array.pop(indeks)
    if i == 1:
        count += 1
    indeks += 1

my_array.reverse()
for i in my_array:
    print(i)