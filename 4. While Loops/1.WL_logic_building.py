"""1. Building Logic with while Loop in Python

The while loop allows you to repeat a block of code as 
long as a specified condition is True. 
It’s useful when the number of iterations is not known beforehand, 
and the loop runs until a condition is no longer met."""

# Print numbers from 1 to 5
i = 1
while i <= 5:
    print (i)
    i += 1 # Increament to avoid infinite loop
    
"""2. Breaking a loop with break
The break statement is used to exit the loop early,
regardless of the loop's condition"""

 # Break out of loop if numbre 3 is encountered
i = 1
while i <=5:
    if i  == 3:
        break # Exit the loop if i is 3
    print(i)
    i += 1 
    
"""3.Skipping an Iteration with continue
The continue statement is used to skip the current iteration 
and move to the next one without exiting the loop"""

# Skip printing number 3
i = 1
while i <= 5:
    if i == 3:
        i +=1
        continue # Skip this iteration when i is 3
    print(i)
    i += 1
    
"""4.Loop with User Input (Using while for Validation)"""

# Repeat until the user enters a valid number
while True:
    num = input("Enter a positive number: ")
    if num.isdigit() and int(num) > 0:
        print(f"Thank you! You entered {num}.")
        break
    else: 
        print("Invalid input! Please enter a positive number.")
        
"""5.Nested while Loop
    You can also nest a while loop inside  another while loop"""
    
# Print a multiplication table (nested loop example)
i = 1
while  i <= 5:
    j = 1
    while j <= 5:
        print(i * j,end= " ")
        j += 1
    print()
    i += 1
    
"""6.Infinite Loop
     An infinite loop occurs when the condition is always true.
     You can use a break statement or a condition to escape from it"""
     
# Escape an infinite loop(with a break)
while True:
    response = input("Do you want to continue?(yes/no): ").lower()
    if response == "no":
       print("Exiting the loop")
       break
    else:
       print("Continuing the loop.") 