'''DEBUGGING IN PYTHON
bug is an error
Finding and fixing bugs is called debugging
Types of errors:
1SYNTAX ERROR:
--> missing colon at the end of a statement
--> misspelled keywords
---> unmatched parentheses, quotes etc, indentation errors.
2RUNTIME ERROR:
--> occur during program execution
--> division by zero, file not found etc.
3LOGICAL ERROR:
--> program runs without error but produces incorrect results
--> incorrect formula, wrong variable used etc.
Debugging techniques:
1. print()
--> 
2. try -except block
3. using pdb
--> Pause the execution
'''

'''try:
    a=int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
    '''
#pdb commands:
'''
1. n--> execution in a next line
2. p variable_name --> print value of variable
3. l -->list nearby code
4. c --> continue execution until next breakpoint
5. s --> start with the function
6. r -->return from the function
7. h --> display help
8. q -->Quit debugging session
'''
import pdb
def add(a,b):
    pdb.set_trace() #Setting a breaking point for debugging
    return a+b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(add(a,b))