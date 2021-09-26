'''
-----------------------------
Author  : Shuvo Kumar Shill 
Date    : 26.09.2021
Subject : String
Class   : 03
------------------------------
'''
# string variable declear
s = "have a nice DAY"
print('Orginal text         :    '+s)
print('Upper case text      :    '+s.upper())
print('lower case text      :    '+s.lower())
print('capitalize case text :    '+s.capitalize())
print('casefold case text   :    '+s.casefold())
print('title case text      :    '+s.title())
print('swapcase case text   :    '+s.swapcase())
print('Count a              :    '+str(s.count('a')))
print('Count A              :    '+str(s.count('A')))
print('len                  :    '+str(len(s)))
print('Center               :    '+s.center(50))
print('Center #             :    '+s.center(50,'#'))
print('Replace              :    '+s.replace('nice', 'good'))
print('Index                :    '+str(s.index('nice')))
print('Find Nice            :    '+str(s.find('Nice')))
print('Split                :    '+str(s.split()))
print(dir(s))