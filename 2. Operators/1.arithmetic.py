# 1. List of Arithmetic Operators

"""
Operator	Description	                     Example
+	        Addition	                     5 + 3 = 8  
-	        Subtraction	                     10 - 4 = 6
*       	Multiplication	                 6 * 2 = 12
/ 	        Division (float result)	         10 / 4 = 2.5
//      	Floor Division (integer result)  10 // 4 = 2
%	        Modulus (remainder)	             10 % 3 = 1
**      	Exponentiation (power)	         2 ** 3 = 8
"""

#2.examples of arithetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Substration:", a - b)
print("Multiplication:", a * b)
print("Division:",a/ b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 3. Floor Division(//) vs Normal division(/)
print(10 / 3)  # Output: 3.3333
print(10 // 3)  # Output: 3

# 4. Using Arithmetic Operators with User Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Power:", num1 ** num2)

# 5. Operator Precedence (Order of Operations)
result = 5 + 2 * 3 
print(result) 

result = (5 + 2) * 3 
print(result) 

# 6. Arithmetic Operators with Strings
print("Hello" + " " + "World")  # String Concatenation (+)
print("Python! " * 3) # String Repetition (*)




