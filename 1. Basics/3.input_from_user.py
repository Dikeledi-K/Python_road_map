"""The input() function in Python is used to take user input. 
It reads input as a string by default."""

# 1.Basic Syntax 
name = input("Enter your name: ")
print("Hello,", name)

# 2.Getting numeric input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

height = float(input("Enter your height in meters: "))
print("Your height is", height, "m")

# 3.Taking multiple inputs
"""You can take multiple inputs using .split()"""
x, y = input("Enter two numbers separated by space: ").split()
print("You entered:", x, "and", y)


"""if you need integers"""
x,y = map(int, input("Enter two numbers seperated by space: ").split())
print("sum: ", x +y)

# 4. Taking input as a list
numbers = list(map(int, input("Enter numbers seperated by space: ").split()))
print("Numbers:", numbers)

# 5.Validating user input
"""To ensure a valid input, you can use a loop"""
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    print("Invalid input! Please enter a number")
print("Your age:", age)

# 6.Hiding password input
"""For secure input like passwords, use 'getpass'"""
import getpass
password = getpass.getpass("Enter your password: ")
print("Password received")