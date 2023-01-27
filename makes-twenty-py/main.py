'''
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False

'''

def makes_twenty(n, m):
    if (n + m == 20) or (n == 20) or (m == 20):
        return True
    else:
        return False

import numpy as np 
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f'Given numbers are {num1}, {num2}')

result = makes_twenty(num1, num2)

print(result)