'''
File Handling Using Python
Date: 19.10.2021
Author: Shuvo Kumar Shill
---------------------------
To Open a file object in pythhon is 

file_object = open('File Name','mode')
The mode are : 
'r' ---> Read mode
'w' ---> write mode
'a' ---> append mode

'''
f = open('shuvo.txt','w')

f.write('This is our new text file\n')
f.write('This is another line\n')
f.write('Hello world\n')
f.write('End line\n')
f.close()

# Open a file for read mode

file = open('shuvo.txt','r')
print(file.read())
# print(file.read(7))

# print(file.readlines()) --> read as list
file.close()

# add some more data
f = open('shuvo.txt','a')

f.write('New line\n')
f.write('Bangladesh\n')
f.write('Dhaka\n')
f.write('Faridpur\n')
f.write('End line 2nd part\n')
f.close()