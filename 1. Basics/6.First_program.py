"""1. The Classic "Hello, World!" Program"""

# The most basic Python program prints text to the screen.
print("Hello, World")

"""2. Taking User Input"""

# A program that asks for your name and greets you
name = input("Enter your name: ")
print("Hello", name, "!")

"""3. A Simple Calculator"""

# A program that adds two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of the two numbers is", sum)

"""4. Even or Odd Checker"""

# A program that checks if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("odd number")

"""5. Simple Loop Program"""

# A program that prints numbers from 1 to 5
for i in range(1, 6):
    print(i)

"""6. Find the Largest of Two Numbers"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1, "is larger")
elif num2 > num1:
    print(num2, "is larger")
else:
    print("Both numbers are equal")

"""7. Check if a Number is Positive, Negative, or Zero"""

num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else: 
    print("The number is zero")


"""8. Multiplication Table of a Number"""

num = int(input("Enter a number: "))
for i in range(1,6):
    print(num, "x", i, "=", num * i )

"""9. Simple Guessing Game"""

secret_number = 7 
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess. Try again")

"""10. Calculate the Factorial of a Number"""

num = int(input("Enter a number: "))
factorial = 1

for i in range(1,num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)

