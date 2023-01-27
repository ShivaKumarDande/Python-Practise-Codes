def smallest(n, m):
    result = 0
    if (n % 2 == 0) and (m % 2 == 0):
        if(n > m):
            result = m
        else:
            result = n
    
    if (n % 2 == 0) and (m % 2 != 0):
        result = n
    elif (n % 2 != 0) and (m % 2 == 0):
        result = m

    return result

import numpy as np
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(a, b)
print(f'The smallest even number of the given two numbers is {smallest(a,b)}')