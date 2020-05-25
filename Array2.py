from array import *

arr = array('i', [])

a = int(input("Enter the Length:-"))

for i in range(a):
    val = int(input("Enter the Array Value:-"))
    arr.append(val)

print("-------arr elements-------")
for i in arr:
    print(i, end=" ")


print("\n---------------Search Value in array-----------------")

s = int(input("Search The Value:-"))

k = 0
for i in arr:
    if i == s:
        print(k)

    k += 1

help(array)

