'''Count freq of each ele in list
input [1,2,4,3,1,2,5]=> {1:2, 2:2, 3:1, 4:1,  5:1}'''
'''def count_frequency(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
li=[1,2,4,3,1,2,5]
print(count_frequency(li))

li=[1,2,4,3,1,2,5]
d={}
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1  
print(d)

d1={}
for i in li:
    d1[i]=d1.get(i,0)+1
print(d1)

from collections import Counter
print(Counter(li))
'''
#find all distinct elements in list without using set
#li=[1,2,4,3,1,2,5] ==> [1,2,3,4,5]
'''li=[1,2,4,3,1,2,5]
freq=[]
for i in li:
    if i not in freq:
        freq.append(i)
print(freq)
'''
'''li=list(list(map(int,input("Enter elements of the list separated by space: ").split())))
s=set()
for ele in li:
    s.add(ele)
print(list(s))
'''

#find the elemrnt with maximum frequency
#[1,2,4,3,1,2,5,1]=> 1
'''from collections import Counter
li=list(map(int,input("Enter elements of the list separated by space: ").split()))
freq=dict(Counter(li))
print(freq.values())
print(max(freq, key=freq.get))

#multiple ele with max freq
max_freq=max(freq.values())
for k in freq:
    if freq[k]==max_freq:
        print(k,end=" ")    '''

