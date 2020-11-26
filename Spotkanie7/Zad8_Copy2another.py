#https://docs.python.org/3/library/array.html
import array
my_arr = array.array('i', [1,3,5,7,9])
my_arr.insert(1,4)
for x in my_arr:
    print(x)