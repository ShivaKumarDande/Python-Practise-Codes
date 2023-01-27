'''
ANIMAL CRACKERS: Write a function takes a two-word string 
and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''

def wordCheck(mylist):
    print(mylist[0][0])
    print(mylist[1][0])
    print(type(mylist[0][0]))
    if( ord(mylist[0][0]) in range (65, 91) and ord(mylist[1][0]) in range(65, 91)):
        return True
    else:
        return False
    
import numpy as np
check = True

while(check == True):
    string = str(input('Enter the two word String : '))
    myWordList = string.split()
    print(len(myWordList))
    if(len(myWordList) != 2):
        print('Please enter a string containing two words')
    else:
        check = False

print(f'Entered string is {string}\n')

result = wordCheck(myWordList)

print(result)