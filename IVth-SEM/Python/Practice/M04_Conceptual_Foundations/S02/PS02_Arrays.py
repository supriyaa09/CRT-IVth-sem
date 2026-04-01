'''Arrays:
1) Reverse the array elements
a. using slicing
b. using loop'''

#input : [12,45,36,78,96]
#output : [96,78,36,45,12]
#without using built-in func and slice range
arr=[12,45,36,78,96]
'''r_arr=[]
stop=-1*len(arr)-1
for i in range(-1, stop, -1):
    r_arr.append(arr[i])
print(r_arr)

res1=[arr[i] for i in range(-1, stop, -1)]
print(res1)

#using swapping
for i in range(len(arr)//2):
    arr[i], arr[-1-i] = arr[-1-i], arr[i]
print(arr)
'''
'''li=[12,45,36,78,96]
res=[]
for ele in li:
    res.insert(0,ele)
print(res)

for ele in li:
    [ele]+res
print(res)

#check whether li is sorted or not
def is_sorted(li):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True

#checking if list is in ascending order
print(is_sorted([12,45,36,78,96,69,100])) #-> False
'''

'''input: [1,2,3,4,1,2,5,2,4]
output: {1:2, 2:3, 3:1, 4:2, 5:1}
'''
li=[1,2,3,4,1,2,5,2,4]
f={}
for ele in li:
    if ele in f:
        f[ele]+=1
    else:
        f[ele]=1
print(f)

'''leetcode:724,1822'''