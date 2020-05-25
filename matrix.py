from numpy import *

m = matrix('1 2 3; 6 4 5; 1 6 7')
print(m)
print(m.diagonal())
print(m.min())
print(m.max())

print("------------Matrix Multiplication--------------------")
m1 = matrix('1 2 3 5; 6 4 5 6; 1 6 7 7; 3 2 5 8')
m2 = matrix('1 2 3 5; 5 6 3 6; 4 5 3 7; 2 4 5 8')
m3 = m1 * m2;
print(m3)