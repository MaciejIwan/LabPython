array = [1,2,3,4]
print(array)
print(array[0],array[1], array[2])

array.append(5)
print(array)

import array
my_array = array.array('i', [1,2,3,4,5])
my_array.append(2)
for i in my_array:
    print(i)