##https://docs.python.org/3/library/array.html
import array as a
my_arr = a.array('i', [1,3,5,7,9])
for x in my_arr:
    print(x)

print("\nPo usunęciu:")
my_arr.pop(2)
for x in my_arr:
    print(x)