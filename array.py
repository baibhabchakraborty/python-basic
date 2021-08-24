from array import *

vals = array('i',[])
n = int(input("Enter length of array:"))

for i in range(n):
    x = int(input("Enter next array value:"))
    vals.append(x)

print(vals)

arr = int(input("Enter element to search:"))
k = 0
for e in vals:
    if(e == arr):
        print(k)
        break
    k+=1

