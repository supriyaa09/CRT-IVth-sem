'''Arthemetic Series
input: 1 2
output: 1 3 5 7 9..
a=1 d=2
1=a+0*d
3=a+1*d'''
'''a=int(input("Enter the first term:"))
d=int(input("Enter the common difference:"))
n=int(input("Enter the number of terms:"))
for i in range(1,11):
    print(a+(i-1)*d,end="")
'''
'''Geometric Series:
input: a=1 r=2
output: '''
'''a=int(input("Enter the first term:"))
r=int(input("Enter the common ratio:"))
n=int(input("Enter the number of terms:"))
for i in range(1,n+1):
    print(a*(r**(i-1)),end=" ")
'''
'''Fibonacci Series:
input n=5
output: 0 1 1 2 3'''
'''n=int(input("Enter no of terms:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
'''
#Fibonacci using list
'''n=int(input("Enter no of terms:"))
l=[0,1]
for i in range(2,n):
    l.append(l[i-2]+l[i-1])
print(l)'''

#Factorial of a number:
n=int(input("Enter a number:"))
'''fact=1
for i in range(1,n+1,1):
    fact=fact*i
print(fact)'''
if n<0:
    print("Factorial not defined for negative numbers")
elif n==0 or n==1:
    print(1)
else:
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    print(fact)
