'''
BLACKJACK: Given three integers between 1 and 11, 
if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def blackjack(myList):
    sum1 = sum(myList)
    sum2 = 1
    if (sum1 <= 21):
        result = sum1
    elif (11 in myList):
        sum2 = sum1 - 10
        
        if (sum2 > 21):
            result = 'BUST'
        else:
            result = sum2
    
    return result
    
import numpy as np
print("Enter the numbers : ")
mylist = []

for i in range(3):
    num = int(input())
    mylist.append(num)

print(f'Entered numbers are : {mylist}')
result = blackjack(mylist)
print(result)