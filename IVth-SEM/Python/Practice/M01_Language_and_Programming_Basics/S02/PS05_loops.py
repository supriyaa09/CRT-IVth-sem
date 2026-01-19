#while -> condition -> till it is true
#for -> count known -> range/iterable -> range(start,stop,step) ->iterable [ 10,20,30] travel every obj in it -> if terminate is not defined then infinite loop
#while condition:  <-syntax
   #code
   #updating condition
#while loop:
'''counter=0
while counter<2:
    print("While Loop")
    counter+=1
'''


'''Read 2 integers start and stop variables. display all even numbers between start and stop (both inclusive)
Input 1 10
Output 2 4 6 8 10
'''
'''start=int(input())
stop=int(input())
while start<=stop:
    if start %2==0:
        print(start,end=" ")
    start+=1
print()'''


'''if multiple of 3 print "Fizz"
if multiple of 5 print "Buzz"  
if multiple of both 3 and 5 print "FizzBuzz"
else print the number itself'''
'''start=int(input())
stop=int(input())
while start<=stop:
    if start %3 ==0 and start %5==0:
        print("FizzBuzz",end=" ")
    elif start %3==0:
        print("Fizz",end=" ")
    elif start %5==0:
        print("Buzz",end=" ")
    else:
        print(start,end=" ")
    start+=1
'''
#for loop:
'''Syntax:
for i in range(start or(default 0),stop (stop is excluded),step or(default 1)):'''
#for i in range(0,5,1):
#    print("Hello World!")

'''start=int(input())
stop=int(input())
for i  in range(start,stop+1,1):
    if i%2==0:
        print(i,end=" ")'''
#Display n natural numbers in same line using for loop
'''n=int(input())
for i in range(1,n+1,1):
    print(i,end=" ")
print()
'''
#Display n natural numbers in reverse order in same line using for loop
'''n=int(input())
for i in range(n,0,-1):
    print(i,end=" ")
'''
#print even numbers from list using for loop (Fetching elements from list)
l=[1,4,6,3,9,2]
for i in range(0,len(l),1):
    if l[i]%2==0:
        print(l[i],end=" ")

