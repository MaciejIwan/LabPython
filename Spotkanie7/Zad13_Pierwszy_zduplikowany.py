#https://docs.python.org/3/library/array.html
import array


def find_duplicate(arr):
    for i in arr:
        if arr.count(i) != 1:
            print(i)
            return
    print("No duplicate")
    return


my_array = array.array('i',  [1,2,3,4,5,6,6])
my_array2 = array.array('i',  [10,11,10,13,14])
my_array3 = array.array('i',  [1,2,3,4,5])

find_duplicate(my_array)
find_duplicate(my_array2)
find_duplicate(my_array3)