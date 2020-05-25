from numpy import *
arr = array([
            [1, 2, 3, 4, 5, 6],
            [11, 12, 13, 14, 15, 16]
            ])
arr1 = arr
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

print("------------convert 2dim array into 1dim array------------")
print(arr1.flatten())

print("-----------convert 1dim array into 3dim array--------------")
print(arr1.reshape(3, 4))

print("------------make 2 2d array in make 2 2d array in 3 elements--------")
print(arr1.reshape(2, 2, 3))