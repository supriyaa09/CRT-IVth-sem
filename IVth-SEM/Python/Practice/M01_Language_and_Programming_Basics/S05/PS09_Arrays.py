'''It is a collection of homogenous data elements that can be stored under a single variable 
Python does not support arrays
Numpy: Numerical Python
it can easily access arrays
mainly used in ML,DS,AI Applications

the index values start with 0 and ens with n-1,n-->Size of an array.
'''
import numpy as np
a=np.array([1,2,3,4])
print(a)
print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.sum(a))
print(np.zeros(5)) # array of 5 elements with all values as 0
print(np.ones(4)) # array of 4 elements with all values as 1
print("Even numbers from 2 to 20:",np.arange(2,10,2)) # even numbers from 2 to 20
print("Odd numbers from 1 to 19:",np.arange(1,10,2)) # odd numbers from 1 to 19
#User input using numpy array
n=int(input("Enter the size of an array:"))
e=list(map(int,input("Enter the elements:").split()))
print("Array elements are:",np.array(e))