#while -> condition -> till it is true
#for -> count known -> range/iterable -> range(start,stop,step) ->iterable [ 10,20,30] travel every obj in it -> if terminate is not defined then infinite loop
#while condition:  <-syntax
   #code
   #updating condition
#while loop:
counter=0
while counter<2:
    print("While Loop")
    counter+=1

'''
Read 2 integers start and stop variables. display all even numbers between start and stop (both inclusive)
Input 1 10
Output 2 4 6 8 10'''
c=2
while c<=10:
        print(c,end=" ")
        c+=2