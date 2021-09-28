''' 
Author: Shuvo Kumar Shill
Example of Nested if
Date:28.09.2021
'''
username=input('Enter You User Name     : ')
password = input('Enter your password   : ')
if username.upper()=='admin'.upper():
    if password == 'shuvo':
        print(f'Welcome Mr. {username}')
    else:
        print('invalid Password')
else:
    print('Invalid user')