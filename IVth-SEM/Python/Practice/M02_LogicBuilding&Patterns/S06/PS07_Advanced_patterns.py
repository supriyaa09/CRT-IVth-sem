'''
1.Pascal Triangle
input: 5
output:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
'''n=int(input("Enter rows: "))
for i in range(1,n+1):
    c=1
    for j in range(i):
        print(c,end=" ")
        c=c*(i-j-1)//(j+1) #(0-0-1//1) (1*4//1=4) (4*3//2=6) (6*2//3=4) (4*1//4=1)
    print()
'''

'''2.Butterfly pattern
n=4
Output:
*      *
**    **
***  ***
**** ****
**** ****
***  ***
**    **
*      *           i n->1 inc +1 and then dec -1'''

n=int(input("Enter rows: "))
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
for j in range(n,0,-1):
    print("*"*j+" "*(2*(n-j))+"*"*j)