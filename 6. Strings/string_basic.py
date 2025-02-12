"""String is a sequence of characters enclosed in a single,
double or tripple quotes.
Strings are immutable - they can not be modified after creation"""

"""1. String basics"""

# Creating strings
str1 = "Hello, World"

# Accesing characyers(Indexing)
text = "Python"
print(text[0])
print(text[-1])

"""2. String literals"""

# Raw strings(r"...") -  used to ignore escape sequences like \n or \t
raw_string = r"Hello\nWorld"
print(raw_string)

# Formatted string literals(f"...") -  used to insert
# variables directly into a string
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

"""3. String operations"""

# Concatenation
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# Repetition
print("Ha" * 3)

# Membership operators( in, not in)
text = "Python is fun"
print("Python" in text)
print("Java" in text)

# Comparison(==, !=, <, >)
print("apple" == "Apple")
print("cat" > "bat")

"""4. String slicing & comprehension"""

# Slicing
text =  "Hello, World"

print(text[0:5])    
print(text[:5])     
print(text[7:])     
print(text[-6:])   
print(text[::-1])

# String comprehension(List of characters)
text = "Python"
letters = [char for char in text]
print(letters)

"""5. String methods"""

"""Method	    Description	                           Example
lower()      	Converts to lowercase	               "HELLO".lower() → "hello"
upper()	        Converts to uppercase	               "hello".upper() → "HELLO"
capitalize()	Capitalizes first letter	           "python".capitalize() → "Python"
title()	        Capitalizes first letter of each word  "hello world".title() → "Hello World"
strip()	        Removes whitespace from both sides	   " hello ".strip() → "hello"
replace(a, b)	Replaces a with b	                   "hello".replace('l', 'r') → "herro"
split(delim)	Splits string into list	               "a,b,c".split(',') → ['a', 'b', 'c']
join(iterable)	Joins elements with separator	       "-".join(['a', 'b', 'c']) → "a-b-c"
find(sub)	    Finds first index of sub	           "hello".find('e') → 1
count(sub)	    Counts occurrences of sub	           "hello".count('l') → 2
startswith(sub)	Checks if starts with sub	           "hello".startswith('h') → True
endswith(sub)	Checks if ends with sub	               "hello".endswith('o') → True"""

# Examples of Common Methods

text = "  Python Programming  "

print(text.lower())    
print(text.strip())   
print(text.replace("Python", "Java"))  
print(text.split())    
print("-".join(["A", "B", "C"]))  

"""6. Checking if a String Contains Only Certain Characters

Method	    Description	      Example
isalpha()	Only letters	  "hello".isalpha() → True
isdigit()	Only digits	      "123".isdigit() → True
isalnum()	Letters + digits  "abc123".isalnum() → True
isspace()	Only spaces	      " ".isspace() → True"""

print("hello123".isalnum())  
print("123".isdigit())       
print("hello world".isalpha())  

"""7. Converting Between Strings and Lists

    Convert string to list: split()
    Convert list to string: join()  """
    
text = "apple,banana,grape"
words = text.split(",")  
print(words)  

new_text = " | ".join(words)  
print(new_text) 

