#https://docs.python.org/3/library/array.html
import array as a
my_arr = a.array('i',  [1,3,5,3,7,1,9,3])
for i in my_arr:
    print(i)
my_list = my_arr.tolist()
print(my_list)
print(type(my_list))