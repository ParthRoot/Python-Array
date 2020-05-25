from numpy import *

arr = array([
            [1, 2, 3, 4, 5, 6],
            [11, 12, 13, 14, 15, 16]
            ])
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

print("------------convert 2dim array into 1dim array------------")
arr1 = arr.flatten()
print(arr1)

print("------------convert 1dim array into 2dim array and 3 elements------------")
print(arr1.reshape(2, 6))
print("------------------------------------")
print(arr1.reshape(2, 2, 3))