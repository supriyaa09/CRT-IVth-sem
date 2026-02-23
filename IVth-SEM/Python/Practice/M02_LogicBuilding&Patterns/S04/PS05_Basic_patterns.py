'''Square star pattern
n=4
* * * *
* * * *
* * * *           for i ->0-n
* * * *           inner loop ->0-n or 1-n+1'''
'''n=int(input("Enter the number of rows:"))
for i in range(0,n,1):
    for j in range(0,n,1):
        print("*",end=" ")
    print()
'''
'''Right angle triangle pattern
n=4
Output:
*
* *
* * *
* * * *           for i ->0-n
*                for j ->0-i or 1-i+1'''
'''n=int(input("enter rows: "))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end=" ")
    print()'''
#Hallow square pattern
'''n=4
Output:
* * * *
*     *
*     *
* * * *  '''
'''n=int(input("enter rows: "))
for i in range(0,n,1):
    if i==0 or i==n-1:
        print("* "*n)
    else:
        print("* "+("  "*(n-2))+"*")
'''
'''Inverted triangle pattern
n=4
output:
* * * *
* * *
* *
*           for i ->0-n
*               for j ->0-n-i or 1-n-i+1'''
'''n=int(input("Enter rows:"))
for i in range(0,n,1):
    for j in range(0,n-i,1):
        print("*",end=" ")
    print()
    '''
#Number triangle pattern
'''n=4
output:
1
1 2
1 2 3
1 2 3 4          '''
n=int(input("Enter rows:"))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print(j+1,end=" ")
    print()