''''   Factors and Primes:
Factors are numbers that divide another number completely without leaving a remainder. For example, the factors of 12 are 1, 2, 3, 4, 6, and 12.
Prime numbers are numbers greater than 1 that have only two factors: 1 and themselves. For example, the prime numbers less than 20 are 2, 3, 5, 7, 11, 13, 17, and 19.'''
'''Factor of 12 -->1,2,3,4,6,12'''
"Print factor of a given number"


'''n=int(input("Enter a number:"))
for i in range(1,n+1,1):
    if n%i==0:
        print(i,end=" ")
'''
#Optimal solution of the same question:
'''n=int(input("Enter a value:"))
for i in range(1,n//2+1,1):
    if n%i==0:
        print(i)
print(n)
'''
#Count of factors of a given number:
'''n=int(input("Enter a number:"))
c=0
for i in range(1,n//2+1,1):
    if n%i==0:
        c+=1
print(c+1)'''
#Prime or not:
'''n=int(input("Enter a number:"))
if n<2:
    print("Not prime")
else:
    for i in range(2,n+1,1):
        if n%i==0:
            break
    if i==n:
        print("Prime")
    else:
        print("Not prime")
'''
'''n=int(input("Enter a number:"))
c=0
for i in range(2,n//2+1,1):
    if n%i==0:
        c+=1
print("prime" if c==0 else "Not prime")'''
'''if c==0:
    print("Prime") #Ternary operator can also be used here
else:
    print("Not prime")
'''

#Print all prime numbers in given range:
'''start=int(input("Enter a number:"))
end=int(input("Enter a number:"))
for n in range(start, end+1, 1): #Outter loop for range of values
    c=0
    for i in range(2,n//2+1,1): #Inner loop for checking if the number is prime or not
        if n%i==0:
            c+=1
    if c==0:
        print(n,end=" ")
'''
#Read a number from the user and display factorial of that number:
'''n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print(fact)

#GCD of 2 numbers:'''
'''input: 12 24
Output:12'''













a=10
b=20
print(a+b)