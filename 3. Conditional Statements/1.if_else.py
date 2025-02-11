"""The if-else statement is used for decision-making in Python.
 It allows a program to execute different blocks of code based on conditions."""

# Check if number is positive

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")

"""if-elif-else (Multiple Conditions)"""

# Check if a number is positive, negarive or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

"""Nested if-else (if inside if)"""

# Check if a number is even or odd, and if it's positive or negative
num = int(input("Enter a number: "))

if num >=0:
    if num % 2 ==0:
        print("The number is even and positive number")
    else: 
        print("The number is odd and positive")
else:
    print("The number is negative")

"""Using if-else with Logical Operators"""

# Check if a number is in a range
num = int(input("Enter a number"))
if num > 0 and num < 101:
    print("The number is between 1 and 100")
else:
    print("The number is out of range")

"""if-else in One Line (Ternary Operator)"""

# Find the maximum of two numbers
a,b = 10, 20
max_num = a if a > b else b
print("The maximum number is: ", max_num)