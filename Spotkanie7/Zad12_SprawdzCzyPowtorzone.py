#https://docs.python.org/3/library/array.html
import array


def is_redundant(arr):
    for i in arr:
        if arr.count(i) != 1:
            return True
    return False


my_array = array.array('i',  [1,2,3,4,5,5])
my_array2 = array.array('i',  [10,11,10,13])
print(is_redundant(my_array))
print(is_redundant(my_array2))