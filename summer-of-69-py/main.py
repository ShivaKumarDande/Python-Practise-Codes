'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''

def summer_69 (mylist):
    sum1 = 0
    if (6 in mylist):
        n = mylist.index(6)
    if (9 in mylist):
        m = mylist.index(9)
    
    for i in range(len(mylist)):
        if (i in range(n,m+1)):
            pass
        else:
            sum1 += mylist[i]
            
    return sum1

import numpy as np 
n = int(input('Enter the number of elements in the array : '))
mylist = []
for i in range(n):
    mylist.append(int(input()))

print(f'Entered array is : {mylist}')

result = summer_69(mylist)
print(result)