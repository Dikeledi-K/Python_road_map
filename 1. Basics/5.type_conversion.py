"""Type conversion(also called type casting) is the 
process of converting a variable from one data type to another"""

"""1. Types of conversion

1. Implicit Type Conversion - Done automatically by python
2. explicit TYpe Conversion - Done manually using functions like int(),
                              float(),str(),etc"""

"""2. Implicit Type Conversion - Python automatically converts 
smaller data types to larger data types to prevent data loss""" 

# Converting int to float
num_int = 10
num_float = num_int + 5.5
print(num_float)
print(type(num_float))

# Converting int to complex
num = 10
complex_num = num + 3j
print(complex_num)
print(type(complex_num))

"""3. explicit Type Concersion(Type casting)

Function	Converts To

int(x)	    Converts x to an integer
float(x)	Converts x to a float
str(x)	    Converts x to a string
list(x)	    Converts x to a list
tuple(x)	Converts x to a tuple
set(x)	    Converts x to a set
dict(x)	    Converts x to a dictionary
bool(x)	    Converts x to a boolean
"""

# 4. Converting between Numeric Types

# Convert float to int
num = 3.9
int_num = int(num) # DRops the decimal, no rounding off
print(int_num)
print(type(int_num))

# Convert int to float
num = 5 
float_num = float(num)
print(float_num)
print(type(float_num))

# Convert int or float to complex
num = 10
complex_numb = complex(num)
print(complex_numb)
print(type(complex_numb))

# 5. Converting between Strings and Numbers

# Convert str to int and float
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(num_int,type(num_int))
print(num_float,type(num_float))

# Convert int or float to str
num = 100
num_str = str(num)
print(num_str, type(num_str))

# Converting between collections

# Convert list to tuple
fruits = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits)
print(fruits_tuple)

# Convert tuple to list
fruits_tuple = ("apple", "banana", "cherry")
fruits_list = list(fruits_tuple)
print(fruits_list)

# Convert list to set
numbers = [1, 2, 3, 2, 1]
numbers_set = set(numbers)
print(numbers_set)

# Convert list of tuples to dict
pairs = [("name", "Alice"),("Age",25)]
person_dict = dict(pairs)
print(person_dict)

# 7.Boolean conversion - Python treats values as True or False.
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))

# 8.Handling Errors in Type Conversion - If conversion is invalid, Python
# throws in error
num_str = "42b"
if num_str.isdigit():
    num = int(num_str) 
    print(num)
else:
    print("Invalid input")