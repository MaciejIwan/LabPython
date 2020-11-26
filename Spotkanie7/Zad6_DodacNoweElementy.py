#https://docs.python.org/3/library/array.html
import array
my_array = array.array('i',  [1, 3, 5, 7, 9])
my_array.extend(my_array)
for i in my_array:
    print(i)
