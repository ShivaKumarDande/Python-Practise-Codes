'''
FIND 33:

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''
def has_33(mylist):
    for i in range(len(mylist)):
        if(mylist[i] == 3 and mylist[i+1] == 3):
            result = True
            break
        else:
            result = False
    return result

import numpy as np
mylist = []
n = int(input('Enter the. number of elements in your list : '))
for i in range(0,n):
    mylist.append(int(input()))

print(f'Entered list of numbers are {mylist}')
result = has_33(mylist)
print(result)