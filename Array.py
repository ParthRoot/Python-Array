from array import *
arr = array('i', [1, 2, -3, 4, 5])
print(arr[0])
print("---------------------------------------")
for i in range(len(arr)):
    print(arr[i])
print("_______________________________________")
i = 0
while i < len(arr):
    print(arr[i])
    i = i + 1

print("_______________________________________")
newArray = array('i', (a for a in arr))
print(newArray)
c = 0
for i in newArray:
    c = c + 1
print(c)




