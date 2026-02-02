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

try:
    a=int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")