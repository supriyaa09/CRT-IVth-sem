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
n=int(input("Enter a number:"))
c=0
for i in range(1,n//2+1,1):
    if n%i==0:
        c+=1
print(c)