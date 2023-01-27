'''
SPY GAME: Write a function that takes in a list of integers
and returns True if it contains 007 in order

 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
 '''

def spyGame_007 (mylist):
    exits0 = False
    if (0 in mylist):
        n = mylist.index(0)
        exits0 = True   #True if 0 exists in the list
    
    if (exits0):    
        if (n < len(mylist) - 2 and mylist[n+1] == 0 and mylist[n+2] == 7):
            result = True
        else:
            result = False
    
    return result

import numpy as np 
n = int(input('Enter the number of elements in an array : '))
mylist = []
for i in range (n):
    mylist.append(int(input()))
    
print(f'Entered array elements are : {mylist}')
result = spyGame_007(mylist)
print(result)