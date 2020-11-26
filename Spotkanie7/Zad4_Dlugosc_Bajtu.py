import array as a
import sys
array_num = a.array('i', [1,3,4,5,7])
array = [1,3,5,7,9]
print("list: ",sys.getsizeof(int()))
x = 5
print("list: ",sys.getsizeof(int(x)))
print(array_num)
print("Array: ",type(array_num))
print("Array: ",type((array_num[0])))
print("Array: ",sys.getsizeof(array_num[0]))
print("Array: ",sys.getsizeof(array_num))

print("\n\n")
print(array)
print("list: ",type(array))
print("list: ",type((array[0])))
print("list: ",sys.getsizeof(array[0]))
print("list: ",sys.getsizeof(array))
print("\n\n")
#========================================================
my_array = a.array('i',  [1, 3, 5, 7, 9])

for i in my_array:
    print(i)
print("\n{}".format(str(my_array.itemsize)))