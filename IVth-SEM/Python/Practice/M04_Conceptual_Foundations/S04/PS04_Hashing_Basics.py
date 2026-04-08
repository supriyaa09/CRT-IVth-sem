'''li=[27,32,46,36,48,55]
dict->immutable->(numeric, string, tuple, frozenset)
d={}->empty dict'''
'''d={1:"a",[1,2]:"b"}
print(d) #-> TypeError: unhashable type: 'list' '''

d={1:'a',2:'b',3:'c',1:'z'}
print(d) #-> {1:'z', 2:'b', 3:'c'}
print(d[1]) #-> 'z'

def instruction(nums1,nums2):
    s1=set(nums1)
    s2=set(nums2)
    print(list(s1.intersection(s2)))
instruction([1,2,2,1],[2,2])

'''leetcode : 1==> Two Sum'''