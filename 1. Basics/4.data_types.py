"""Data types - the nature of the data stored in variables"""


# 1.Built in data types in python
"""
Category    Data Types
	
Numeric	    int, float, complex
Sequence	str, list, tuple, range
Set Types	set, frozenset
Mapping   	dict
Boolean	    bool
Binary	    bytes, bytearray, memoryview """

# 2.Numeric types

# integer (int) - whole numbers(positive or negative) without decimals
x = 10
y = -5
print(type(x))

# Floating point(float) - numbers with decimals
pi = 3.14
price = 99.99
print(type(pi))

# Complex numbers(complex) - numbers with real or imaginary part
z = 2 + 3j
print(type(z))

# 3.Sequence types

# string(str) - a sequence of characters enclosed in quotes
text = "HEllo, World"
print(type(text))

# lists - an ordered, mutable(changeable) collection.
fruits = ["Apple", "Banana", "Cherry"]
print(type(fruits))

# lists allows different numbers
mixed_list = [1, "Python", 3.14]
print(type(mixed_list))

# Tuple(tuple) - an ordered, immutable(unchangeable) collection.
coordinates = (10, 20, 30)
print(type(coordinates))

# Ranges(range) - used to generate a sequences of numbers
r = range(5)
print(type(r))

# 4.Set types

# set(set) - an unordered collection of unique elements
colors = {"red", "green", "blue"}
print(type(colors))

# Frozen set(frozenset) - an immutable version of a set
f_set = frozenset({1, 2, 3})
print(type(f_set))

# 5.Dictionary(dict) - a collection of key-value pairs.
person = {"name": "Alice", "age": 25}
print(type(person))

# 6.Boolean(bool) - represents True or False values
is_valid = True
print(type(is_valid))

# 7.Binary types

# bytes(bytes) - Immutable sequences of bytes
b = bytes([65, 66, 67])
print(type(b))

# Bytes Arrays(bytearrray) - a mutable sequence of bytes
ba = bytearray([67, 68, 69])
print(type(ba))

# Memory view(memoryview) -  Used for handling large binary 
# data efficiently
m = memoryview(b"Hello")
print(type(m))

# 8.None type(NoneTypes) - represents an absence of a value
value = None
print(type(value))

# 9.Checking and Coverting Data Type

"""Type Conversion(Casting)"""

# Convert string to int
num = int("42")
print(type(num))

# Convert int to string
text = str(100)
print(type(text))

# Convert list to tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(type(tup))
















