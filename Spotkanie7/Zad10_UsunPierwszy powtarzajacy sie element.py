#https://docs.python.org/3/library/array.html
import array as a
my_arr = a.array('i', [100,200,150,95,200])
for i in my_arr:
    if my_arr.count(i) is not 1:
        my_arr.remove(i)

for i in my_arr:
    print(i)