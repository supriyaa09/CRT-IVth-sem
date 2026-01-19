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
start=int(input())
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