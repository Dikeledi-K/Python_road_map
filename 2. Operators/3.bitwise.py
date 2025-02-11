"""
1. List of Bitwise Operators

Operator	Name	    Example (a=5, b=3)	Binary Calculation	Output
&	        AND	        a & b	            0101 & 0011     	0001 (1)
`	        `	        OR	                `a	                b`
^	        XOR	        a ^ b           	0101 ^ 0011	        0110 (6)
~	        NOT 	    a	                ~0101	            1010 (-6)
<<	        Left Shift	a << 1          	0101 << 1	        1010 (10)
>>	        Right Shift	a >> 1          	0101 >> 1	        0010 (2)

"""

# 2. Explanation of Bitwise Operators

"""Bitwise AND (&)
   - Compares each bit of two numbers
   - REturns 1 if both bits are 1, else 0"""
a = 5
b = 3
print(a & b)

"""Bitwise OR (|)
   -Compares each bit of two numbers.
   -Returns 1 if at least one bit is 1."""
print(a|b)

"""Bitwise XOR (^)
   -Compares each bit of two numbers.
   -Returns 1 if bits are different, else 0."""
print(a ^ b)

"""Bitwise NOT (~)
   -Inverts all bits (0 becomes 1, 1 becomes 0).
   -In Python, ~x is -(x+1)"""
print(~a)

