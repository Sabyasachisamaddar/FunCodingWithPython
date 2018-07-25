from  random import *
import numpy as np
#Creating a x size array

size = int(input("What is the size of the array ?"))
arr = [0] * size
for x in range(0,size):
    arr[x] = randint(0,9)
print(arr)
search_number = int(input("What is the number to search ?"))
if(search_number in arr):
    for x in range(0, size):
        if search_number == arr[x]:
            print(x+1)
else:
    print('Number not found!!!')





