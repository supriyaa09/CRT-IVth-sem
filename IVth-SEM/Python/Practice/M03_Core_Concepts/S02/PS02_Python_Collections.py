#1 Creating lists
a=[1,2,3,4,5]
print(a)
b=list((1,2,123))
print(b)

#2 accessing of list
a=[1,2,3,4,5]
print(a[0])  #O(1)
print(a[-1]) #O(1)


t=(10,20,30,40,50)
print(t)
t1=tuple((10,20,30,40,50))
print(t1)
print(t+t1)
print(t[0])  #O(1)
print(t[-1]) #O(1)
print(t+t1)
print(t,t1)
print(t*3)
print(t[0:3])
print(t[1:4])
#del t
#print(t)

#Dictionaries -> collection of key value pairs
d={'name':'Alice','age':30,'city':'New York'}
print(d)
print(d['name'])  #O(1)
print(d.get('age'))  #O(1)
d['age']=31
print(d)
d['country']='USA'
print(d)
del d['city']
print(d)
del d
d1={'name':'Bob','age':25,'city':'Los Angeles'}
print(d1)
d1.clear()
print(d1)



