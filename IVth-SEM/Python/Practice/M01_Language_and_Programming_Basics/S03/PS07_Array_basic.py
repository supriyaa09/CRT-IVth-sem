'''ARRAY==> multiple values in a single variable
1-D array==> list '''
'Create a arr of float type and print the elements of array'
import array
a=array.array('f',[34.5,7.5,6.7,5.6])
print(a,type(a))
a.append(1.2)
print(a)