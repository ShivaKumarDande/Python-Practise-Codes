'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''

def reverseString(string):
    result = ''
    mylist = string.split()
    for i in range(len(mylist)-1, -1, -1):
        result += mylist[i] + ' '

    return result
        

import numpy as np 
myString = input("Enter the string : ")
print(f'Entered string is : {myString}')
result = reverseString(myString)
print(result)