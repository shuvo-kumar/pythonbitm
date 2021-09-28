'''


'''

while True:
    print('Manin Menu')
    print ('1. Addition :   ')
    print ('2. Substraction :    ')
    print ('3. Multiplication : ')
    print ('4. Divistion    :   ')
    print ('5. Modulus  :   ')
    print ('6. Exponent :')

    print('Entre your selection : ', end='')
    
    choice= int(input())

    if choice==1:
        a=int(input('Enter valu for A : '))
        b=int(input('Enter valu for B : '))
        print(f'{a} +{b}',a+b)
    elif choice ==2:
        a=int(input('Enter valu for A : '))
        b=int(input('Enter valu for B : '))
        print(f'{a} - {b}',a-b)
    elif choice ==3:
        a=int(input('Enter valu for A : '))
        b=int(input('Enter valu for B : '))
        print(f'{a} *{b}',a*b)
    elif choice ==4:
        a=int(input('Enter valu for A : '))
        b=int(input('Enter valu for B : '))
        print(f'{a} /{b}',a/b)
    elif choice ==5:
        a=int(input('Enter valu for A : '))
        b=int(input('Enter valu for B : '))
        print(f'{a} %{b}',a%b)
    elif choice ==6:
        a=int(input('Enter valu for A : '))
        b=int(input('Enter valu for B : '))
        print(f'{a} **{b}',a**b)

    elif choice == 7:
        print('Thank You')
        break
    else:
        print("Sorry invalid seclion")        
