'''
Python recursipon
---------------------
A function that calls itselft.

Date: 19.10.2021

'''

# Factorial using loop
# 3! = 3x2x1

fact = 1
# num = 3
num = int(input('Enter value for factorial : '))
for i in range(1,num+1):
    fact = fact*i

print(f'The factorial of {num} is {fact} ')

#  Factorial using recursive method

def factorial (n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

''' 
Factorial (3)
        3*factorial(3-1)
        3*2*factorial(2-1)
        3*2*1 

'''
print(f'The factorial of {num} is {factorial(num)} ')
print(factorial(7))

# HW : using recursive methode output fibonaci element 