print(sum([1, 2, 3, 4, 5]))  # Output: 15
print(abs(-5))  # Output: 5
print(abs(10))

#gcd of 2 numbers
'''8-> 1,2,4,8
10-> 1,2,5,10
'''
'''def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print(gcd(8,10)) #-> 2 '''


#Traditional method to find GCD ->sol 1
'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
min_num=min(a,b)
for i in range(1, min_num+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD:", gcd)

#sol 2
while a!=b:
    a,b =b,a%b
print("GCD:", a)'''

'''LCM:
8==>8,16,24,32,40,48,56,64
10==>10,20,30,40,50,60,70,80,90,100
'''
#Traditional method to find LCM ->sol 1
'''a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
max_num=max(a,b)
while True:
    if max_num%a==0 and max_num%b==0:
        lcm=max_num
        break
    max_num+=1
print("LCM:", lcm)
'''
'''c=int(input("Enter first number: "))
d=int(input("Enter second number: "))
import math
lcm=(c*d)//math.gcd(c,d)
print("LCM:", lcm)
'''

#perfect number
def perfect_number(n):
    sum_of_divisors=0
    for i in range(1, n):
        if n%i==0:
            sum_of_divisors+=i
    return sum_of_divisors==n

# Test the function
print(perfect_number(6))  # Output: True (6 is a perfect number)
print(perfect_number(12))  # Output: False (12 is not a perfect number)

'''
Leetcode: 1071 , 1979'''