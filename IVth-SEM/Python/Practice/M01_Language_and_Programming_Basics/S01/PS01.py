user_name="Alice"
print(user_name)
"""
Data types:
1.fundamental
- int
- float 
-complex    (a+bi in python a+bj)
-Boolean
_String

2.Collection
- list
- tuple
- set
- dictionary
"""
x=10
y=3.14
z=2+3j #complex number
print(type(x))
print(type(y))
print(type(z))
f1=12e1 #12*10^1
f2=5E3 #5*10^3
print(f1,type(f1))
print(f2,type(f2))

c1=5+4j
c2=complex(2,-3)
print(c1,type(c1))
print(c2,type(c2))
print(c1+c2) 
print(c1*c2)
print(c1.real,c1.imag)
print(c1-c2)
print(c1/c2)

#String
s1="Hello, World!"
s2='Python 3.14.2'
s3='''This is a multi-line
string example.'''
print(s1)
print(s2)
print(s3)
print(type(s1))
print(len(s2)) #length of string
print(s1[0]) #indexing
print(s2[0:6]) #slicing
print(s1.lower())
print(s2.upper())
print(s1[0:5:2]) #slicing with step

