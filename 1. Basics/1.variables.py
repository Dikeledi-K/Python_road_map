"""Basic Rules for Variables

1. No need to declare type – Python automatically determines the data type.
2. Names must start with a letter or underscore (_) but cannot start with a number.
3. Can contain letters, numbers, and underscores (_).
4. Case-sensitive (name and Name are different variables).
5. Cannot use Python keywords (e.g., if, for, class, etc.). """

"""1. What is a Variable?
A variable is a named storage in memory that holds a value.
In Python, you don’t need to declare the type of a variable—Python 
infers it automatically."""

message = "Hello, World!"  # String
age = 25                  # Integer
temperature = 36.6        # Float
is_python_fun = True      # Boolean

"""2. Assigning Multiple Variables
You can assign values to multiple variables at once."""

a, b, c = 10, 20, 30  # Assigning multiple values
x = y = z = "Same"    # Assigning the same value to multiple variables


"""3. Changing Variable Types (Dynamic Typing)
Python allows you to change the type of a variable at runtime."""

x = 5        # Integer
x = "Hello"  # Now it's a string
x = 3.14     # Now it's a float

"""4. Variable Naming Rules
✔ Must start with a letter (a-z, A-Z) or underscore (_)
✔ Can contain letters, numbers (0-9), and underscores (_)
❌ Cannot start with a number (1var = 10 ❌)
❌ Cannot use Python keywords (if, for, class, etc.)"""

valid_name = "Python"
_valid_name = "Allowed"
ValidName123 = "Also Allowed"

""" Invalid names
123name = "Error"  # ❌ Starts with a number
class = "Error"    # ❌ 'class' is a reserved keyword """

"""5. Constants (Using ALL CAPS
Python doesn’t have built-in constants, but by convention,
variables meant to be constants are written in ALL_CAPS."""

PI = 3.14159
GRAVITY = 9.8

"""6. Deleting Variables
You can delete a variable using del."""

x = 100
del x  # Now x is removed from memory

"""7. Global vs. Local Variables
Local variables exist inside a function.
Global variables exist outside functions 
and can be accessed inside functions using global. """

x = "global variable"

def my_function():
    global x  # Use the global variable inside a function
    x = "modified globally"

my_function()
print(x)  # Outputs: modified globally

"""8. Type Checking and Conversion
You can check a variable's type using type() and 
convert between types using int(), float(), str(), etc."""

x = 42
print(type(x))  # Output: <class 'int'>

# Type conversion
x = str(x)  # Convert integer to string
y = float(10)  # Convert integer to float

"""9. Special Variables: None
Python has a special value None, 
which represents an empty or undefined value """

x = None
print(x)  # Output: None
print(type(x))  # Output: <class 'NoneType'>

"""10. F-Strings and Variables
Python allows easy string formatting with f-strings """

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  
# Output: My name is Alice and I am 30 years old.
