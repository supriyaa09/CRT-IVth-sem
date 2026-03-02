'''Comprehensions and joined methods:
Comprehensions : List, Set and Dictionary comprehensions are a concise way to create new collections by applying an expression to each item in an iterable. They can also include conditions to filter items.
li=[1,2,3,4,5]
output=[1,4,9,16,25]'''
'''li=list(map(int,input("Enter numbers:").split()))
for i in range(len(li)):
    li[i] = li[i]**2
print(li)

li=[1,2,3,4,5]
res=[]
for i in li:
    res.append(i**2)
print(res)
'''
'''ans=[i**2 for i in li]
print(ans)'''

#li=[1,2,3,4,5] output -[2,4] only even numbers
'''li=list(map(int,input("Enter numbers:").split()))
a=[i for i in li if i%2==0]
print(a)'''

'''res=[]
for i in li:
    if i%2==0:
        res.append(i)
print(res)'''

'''li=[1,2,3,4,5]
for i in range(len(li)):
    if li[i]%2==0:
        print(li[i],end=" ")
'''
#print(" * "*5)
'''li=['a','b','c'] #output-['a b c']
res=""
for ch in li:
    res=res + ch+" "
print(res)

print("@".join(li))'''
'''PAterns:
1. pyramid pattern
n=4
   *
  * *
 * * *
 * * * *           using single loop:'''
'''n=int(input("enter rows:"))
for i in range(1,n+1): #i=1 space =3 so n-i
    print(" "*(n-i)+"* "*i)
''''''
'''


'''reverse pyramid pattern
n=4 
* * * *
 * * *
  * *
   *           i n->1 dec -1'''
'''n=int(input("Enter rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)'''
#'''Diamond pattern
#n=4
#   *
#  * * 
# * * *
#  * *
#   *           i n->1 inc +1 and then dec -1'''
'''n=int(input("enter rows: "))
for i in range(1,n+1,1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
'''
'''number pyramid pattern
n=4 
   1
  1 2
 1 2 3
 1 2 3 4           i n->1 inc +1 and then dec -1'''
'''n=int(input("Enter rows: "))
for i in range(1,n+1):
    print(" "*(n-i)+ " ".join([str(j) for j in range(1,i+1)]))'''

'''Binary triangle pattern
n=4
   1
  0 1
 1 0 1
 0 1 0 1           i n->1 inc +1 and then dec -1
 
 Cross pattern:
 n=5
 *   *
  * *
   *
  * *
  *   *           i n->1 inc +1 and then dec -1
  
  Hollow diamond pattern:
  n=4
    *
    * *
   *   *
    * *
     *
     
Hollow pyramid pattern:
n=4
   *
  * *
 *   *
 * * * *           i n->1 inc +1 and then dec -1'''
n=int(input("Enter rows: "))
for i in range(1,n+1):
    if i==1:
        print(" "*(n-i)+"*")
    elif i==n:
        print("*"*(2*n-1))
    else:
        print(" "*(n-i)+"*"+(" "*(2*i-3))+"*")