"""Basic Rules for Variables

1. No need to declare type – Python automatically determines the data type.
2. Names must start with a letter or underscore (_) but cannot start with a number.
3. Can contain letters, numbers, and underscores (_).
4. Case-sensitive (name and Name are different variables).
5. Cannot use Python keywords (e.g., if, for, class, etc.). """


# Assigning values to variables

x = 10        # Integer
name = "John" # String
pi = 3.14     # Float
is_valid = True # Boolean

# Multiple assignments
a, b, c = 1, 2, 3
x = y = z = "Same Value"

# Using variables in expressions
total = x + 5
greeting = "Hello, " + name

# Dynamic Typing

#Python allows changing the data type of a variable:

x = 10
x = "Now I'm a string!"