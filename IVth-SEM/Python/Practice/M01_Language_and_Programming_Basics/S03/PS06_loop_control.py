'''LOOP CONTROL STATEMENTS:
1.break
loop terminates when break statement is encountered
2.continue
skips the current iteration and moves to next iteration
'''
'''for i in range(1,11,1):
    print(i)  #(prints 1 to 5 if print was below it would have executed till 4)
    if i==5:
        break
'''
'''for i in range(1,11,1):
    if i==5:
        continue
    print(i,end =" ")#(prints 1 to 10 except 5)
else:
    print("Loop completed")
'''
'''username given check if pass is correct print sucessful execution else run loop for 3 attempts
if all attempts fail print "Account locked'''
username="USERNAME101"
password="PASSWORD101"
a=0
for i in range(3):
    Pass=input("Enter password:")
    if Pass==password:
        print("Successful Execution")
        break
    else:
        print("Incorrect passwod!",2-a ,"attempts left.")
        a+=1
if a==3:
    print("Incorrect password! 0 attempts left.Account Locked")
