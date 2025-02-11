"""Relational (Comparison) Operators in Python

Relational operators are used to compare two values and return True or False
 based on the condition."""

"""
1. List of Relational Operators

Operator   Description	             Example
==         Equal to	                 5 == 5 → True
!=	       Not equal to	             5 != 3 → True
>	       Greater than	             10 > 5 → True
<	       Less than	             3 < 8 → True
>=	       Greater than or equal to	 5 >= 5 → True
<=	       Less than or equal to	 4 <= 6 → True

"""

# 2.Example of Relational Operators
a = 10
b = 5

print("a == b:", a == b)   
print("a != b:", a != b)   
print("a > b:", a > b)     
print("a < b:", a < b)    
print("a >= b:", a >= b)   
print("a <= b:", a <= b)

# 3. Relational Operators with User Input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Equal:", num1 == num2)
print("Not Equal:", num1 != num2)
print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)
print("Greater than or equal:", num1 >= num2)
print("Less than or equal:", num1 <= num2)

# 4. Relational Operators with Strings- String comparisons are case sensitive
print("apple" == "apple") 
print("apple" == "Apple")  
print("banana" > "apple")  

# 5. Relational Operators in Conditions -  can be used in if statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else: 
    print("You are a minor")




