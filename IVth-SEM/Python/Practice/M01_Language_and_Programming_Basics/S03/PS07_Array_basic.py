'''ARRAY= multiple values in a single variable
1-D array=list '''
#Create a arr of float type and print the elements of array
'''
import array
a=array.array('f',[34.5,7.5,6.7,5.6])
print(a,type(a))
a.append(1.2)
print(a)
'''
import numpy as np
a1=np.array([1,2,3,4,5])
a2=np.array([[4,5,6],
            [7,8,9],
            [10,11,12]])
print(a1.shape)
print(a2.shape)
print(a2.dtype)