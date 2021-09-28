''' 
Author: Shuvo Kumar Shill
Example of Combanation of condtion
---------------------------------
Date:28.09.2021
'''
username=input('Enter You User Name     : ')
password = input('Enter your password   : ')
if username.upper()=='admin'.upper() and  password == 'shuvo':
        print(f'Welcome Mr. {username}')
else:
    print('Invalid user')