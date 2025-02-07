# 1. Basic usage
print("Hello, World!")

# 2. Printing multiple values
print("Python", "is", "awesome")

# 3. Customizing seperators with 'sep'
print("python", "is", "awesome", sep = "-")
print("Day", "Month", "year", sep = "/")

# 4. Changing End character with 'end'
print("Hello", end = " ") #end = " " prevents new line from being added.
print("World!")

# 5. Printing variables
name = "Alice"
age = 25
print("Name:", name, "Age:",age)

# 6. String Formating in "print()"

# Using f-strings
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

x = 5
y = 10
print(f"The sum of {x} and {y} is {x +y}.")

# Using .formar() method
name = "Bob"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Printing special characters
"""
\n - New line
\t - Tab space
\' - Single quote
\"" - Double quote
\\ - Backslash
"""
print("Hello\nWorld") # New line
print("Hello\tWorld") # Tab space
print("I\'m learning") # Single quote
print('\"Python\" is fun!') # Double quote
print("C:\\Users\\Documents") # Backslash

# 8. Printing Lists, Dictionaries, and Other Data Types

# Printing Lists
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)

# Printing Dictionareies
person = {"name": "Alice", "age": 25,"city": "New York"}
print(person)

# 9. Printring without a Newline
print("Hello", end = "") #newline without space
print("World")

# 10. Printing to a file
with open("output.txt", "w") as file: # This will create a file named output.txt
    print("This will be saved in a file!", file= file) # and write this text inside it.

# Printing Unicode Characters
print("\u2764")
print("\U0001F5600")

# Debugging with "print()"
x = 10
y = 20
print(f"x: {x}, y: {y}, sum: {x + y}")
