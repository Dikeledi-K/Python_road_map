"""Loops in python are used to iterate over 
sequences(like lists, strings, or ranges) and perform repeated 
task efficiently"""

"""1. For loop
A for loop is used when you know howmany times you want to iterate 
or when looping over a sequence."""


# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
# Iterating over a string
word = "Python"
for char in word:
    print(char)
    
"""2. range() function - generates a sequence of numbers"""

"""syntax

range(start, stop, step)"""

for i in range(5):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
for i in range(5, 0, -1):
    print(i)
    
"""3. Nested for loops- is a loop in another loop"""

# Printing a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print() # Empty line afrer each row
    
    
"""4. Pattern-based questions"""

# Right angled triangle
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
    
# Pyramid patterns
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Inverted triangle
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)
    
"""5. Break statement- exits the loop immeidtely when a condition is met"""

# Stopping when number 3 is found
for num in range(1, 6):
    if num ==3:
        break
    print(num)
    
"""6. Continue statement - skips the current iteration 
and moves to the next one"""

# Skipping number 3
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
    
"""7. Pass statement - acts as a placeholder for future code"""

for num in range(5):
    if num == 2:
        pass # Placeholder
    print(num)
    
"""8. else in loops
      used with for and while loops
      the else block executes only if the loop completes normally(
          when no break is encoutered)"""
          
for i in range(1, 6):
    print(i)
else:
    print("Loop finished successfully.")


    
    