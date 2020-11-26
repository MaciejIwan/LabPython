#https://docs.python.org/3/library/array.html
import array
my_array = array.array('i',)
my_list = [1, 2, 6, 8]
my_array.fromlist(my_list)
for i in my_array:
    print(i)
