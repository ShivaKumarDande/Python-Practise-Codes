'''
COUNT PRIMES: Write a function that returns the number of
prime numbers that exist up to and including a given number

count_primes(100) --> 25
'''

def primeNumbers(number):
    n = 0
    b = True
    for i in range(2, number+1):
        b = True
        for j in range(2, int((i)/2)+1):
            if (i % j == 0):
                b = False
        if(b == True):
            print(f'{i}\n')
            n += 1
    return n

import numpy as np 
n = int(input("Enter a number : "))
print(f'Entered number is {n}')
result = primeNumbers(n)
print(result)