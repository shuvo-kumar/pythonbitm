''' 
Author: Shuvo Kumar Shill
Date: 21.10.2021

fibo series
0 1 1 2 3 5 8

a+b=c
b+c=d


a=0
b=1
c=a+b
b=c


'''
def fibo (n):
    n1 = 0
    n2 = 1
    if n<=0:
        return "please enter higher then 0"
    if n==1:
        return 0
    if n ==2:
        return 1
    for i in range(2,n):
        sum = n1 + n2
        n1 =n2
        n2 = sum
    return n2

# print(fibo(int(input('Enter nth fiboo Number : '))))

def fibo1(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo1(n-1)+fibo1(n-2)

print(fibo1(int(input('Enter nth fiboo Number : '))))