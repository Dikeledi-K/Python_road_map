"""1. Function definition and calling
      A function is defined using the def keyword and called by is name."""
      
"""Syntax

def function_name(parameters):
    Docstring - describes function
    #Function body
    return value """
    
# Function defination and call
def greet(name):
    """Prints a greeting message"""
    print(f"Hello, {name}")
    
greet("Dikeledi") # Calling the function

"""2. Function Arguments

Arguments allow functions to receive values when called.
Types of Arguments:

    Positional Arguments - Passed in order.
    Keyword Arguments - Passed with parameter names.
    Default Arguments - Have a default value.
    Variable-Length Arguments (*args, **kwargs) - 
    Handle unknown numbers of arguments."""
    
# Positional Arguments
def add(a, b):
    return a + b
print(add(3, 5))

# Keyword Arguments
def greet(name,age):
    print(f"Name: {name}, Age: {age}")
    
greet(age = 25, name = "Dikeledi")

# Default Arguments - if an argument isn't provided,default value is used.
def greet(name = "Guest"):
    print(f"Hello, {name}")
greet()
greet("Dikeledi")

# Variable-Length Arguments(*args, **kwargs)
# *args - For multiple positional arguments(tuple)
# **kwargs - For multiple keyword arguments(dictionary)
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3, 4))

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
user_info(name = "Dikeledi", age = 25, city = "Johannesburg")

"""3. Function Doctring - Docstrings are used to document functions."""

def square(n):
    """Returns the square of a number"""
    return n * n
print(square.__doc__)

"""4. Scope(Local & Global variables)- defines where variables can be accessed"""

# A local scope (Inside function)
def func():
    x = 10 # local variable
    print(x)
    
func()

# Global scope(Accessible everywhere)
x = 5 # Global variable
def show():
    print(x)
    
show()
print(x)

# Modifying Global variables with global keyword
x = 10 
def change():
    global x
    x = 20
change()
print(x)

"""5. Special functions: Lamda, map(), filter()"""

# Lamda(Anonymous functions)- are one-liner functions without a name
square = lambda x: x * x
print(square(4))

add = lambda a, b: a + b
print(add(3, 5))

# map() function - applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x **2, numbers))
print(squared)

# filter() function - filters elements based on a condition
numbers = [1, 2, 3, 4, 5, 6, 7]
evens = list(filter(lambda x: x % 2 ==0, numbers))
print(evens)

"""6. Recursion(Function caling itself)"""

# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  

# Fibinacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  

"""7. Functional programing"""


