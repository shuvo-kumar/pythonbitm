''' 
Author: Shuvo Kumar Shill
Example of Nested if
Date:28.09.2021
'''
username=input('Enter You User Name     : ')
password = input('Enter your password   : ')
if username.upper()=='admin'.upper() and password =='shuvo':
    print(f'Welcome Mr. {username}')
elif username.upper() != 'admin'.upper() and password == 'shuvo':
    print('invalid user')
elif username.upper() != 'admin'.upper() and password == 'shuvo':
    print('invalid Passwod')
else:
    print('Invalid username or password')