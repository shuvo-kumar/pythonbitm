''' 
Author  : Shuvo Kumar Shill
Date    : homework for thusday
Homework: find big number within 4 numbers
'''
n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))
n3 = int(input("Enter 3rd Number : "))
n4 = int(input("Enter 4th Number : "))

if n1>=n2>=n3>=n4:
    print(f'Your Big Number is {n1}')
elif  n2>=n3>=n4>=n1:
    print(f'Your Big Number is {n2}')
elif  n3>=n4>=n1>=n2:
    print(f'Your Big Number is {n3}')
else:
    print(f'\nYour Big Number is {n4}')
