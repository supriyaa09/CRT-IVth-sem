'''Time Complexity: time required for an algo to run as a function of the length of the input.
Big O Noatation:
O(1) - Constant Time
O(n) - Linear Time
O(n^2) - Quadratic Time
O(log n) - Log Linear Time
O(n log n) - Linearithmic Time
O(2^n) - Exponential Time
O(n!) - Factorial Time'''
# O(1) - Constant Time
def constant_time(arr):
    return arr[0]
print(constant_time([1, 2, 3, 4, 5]))     #O(1)

def linear_time(arr):
    for i in arr:
        print(i)
print(linear_time([1, 2, 3, 4, 5]))       #O(n)

def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i)
print(quadratic_time([1, 2, 3, 4, 5]))    #O(n^2)


def linearithmic_time(arr):
    return sorted(arr)
print(linearithmic_time([5, 4, 3, 2, 1])) #O(n log n)   

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  

n=int(input("Enter the value of n: "))
print(f"Fibonacci of {n} is: {fibonacci(n)}")   #O(2^n)











































