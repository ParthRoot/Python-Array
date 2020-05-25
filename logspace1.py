from numpy import *

arr = array([1, 2, 3, 4, 5])
arr1 = array([])
arr1 = arr
print(arr, id(arr))
print(arr1, id(arr))
print("------------change value---------------")
arr[3] = 55
print(arr, id(arr))
print(arr1, id(arr))
print("------------Using View()---------------")
arr2 = arr1.view()
print(arr1, id(arr))
print(arr2, id(arr2))
print("--------------copy()-------------------")
arr3 = arr1.copy()
print(arr1, id(arr))
print(arr3, id(arr3))
arr1[2] = 566
print(arr1)
print(arr3)


