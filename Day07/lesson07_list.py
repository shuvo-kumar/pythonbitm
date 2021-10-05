'''
List
-------------
listVar = []
'''

motorcycles =['Honda', 'Yamaha', 'Suziki',]

print(motorcycles)
# print(motorcycles[0])
# print(motorcycles[1])
# print(motorcycles[2])

# for motor in motorcycles:
#     print(motor)

i=0
while i<2 :
    print(motorcycles[i])
    i+=1
# change Yamaha to Dhukati
motorcycles[1]='Hero'
print(motorcycles)

# motorcycles.append()

# append() = add list last data

fruits = []
fruits.append('Mango')
fruits.append('Banana')
fruits.append('Grape')
print(fruits)

#  insert(index, 'List item') data any of list index 
fruits.insert(2,"jackfruits")
print(fruits)
fruits.extend(['mango', 'Bangi', 'Dragonfruits', 'apple', 'Grape'])
print(fruits)

# delete using index

del fruits[6]
print(fruits)

# delete using item name
fruits.remove('Bangi')
print(fruits)


# pop-LIFO

fruits.pop() #LIFO


print(fruits)

# show help function/method argument
print(dir(fruits))

print(fruits.count('mango'))
print(fruits.index('mango'))

fruits.reverse()
print(fruits)


fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)


print(f'Total Number of Fruits {len(fruits)}')

# slicing list
print(fruits[-1])
print(fruits[-2])
print(fruits[1:3])
print(fruits[:3])
print(fruits[3:])