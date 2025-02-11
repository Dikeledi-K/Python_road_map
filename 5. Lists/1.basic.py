"""Python Lists - Basics, Operations, Comprehensions, and Methods

A list in Python is a collection that is ordered, mutable (modifiable),
and allows duplicate elements. Lists can store different data types,
including numbers, strings, and even other lists."""

"""1. List basics"""

# Creating a list
my_list = [] # Empty list

numbers = [1, 2, 3, 4, 5]
fruits = ["Apple", "Banana", "Cherry"]
mixed = [1, "Hello", 3.14, True]

# Accessing elements
# Use indexing(starts from o)
# Use negative indexing(starts from -1 for the last element)
print(numbers[0])
print(numbers[-1]) 

# Modifying elements - Lists are mutable, so you can change elements
numbers[2] = 10
print(numbers)

"""2. List operations"""

# Concatenation(+)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) 

# Repetition
print(a * 2)

# Checking membership(in, not in)
print(2 in a)
print(7 not in a)

"""3. List Comprehensions and Slicing"""

# List comprehension(Shorter way to create lists)

# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)

# Even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 ==0]
print(evens)

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6]) # from index 2 to 5
print(numbers[:4]) # first 4 elements
print(numbers[5:]) # from index 5 to end
print(numbers[::2]) # every second element
print(numbers[::-1]) # reversed list

"""4. Common List Methods

Method	         Description	                                Example

append(x)	     Adds an element to the end	                    my_list.append(10)
insert(i, x)	 Inserts element at index i                 	my_list.insert(2, "hello")
extend(iterable) Adds elements from another list	            my_list.extend([7, 8])
remove(x)	     Removes first occurrence of x              	my_list.remove(3)
pop(i)	         Removes and returns element at i	            my_list.pop(1)
index(x)	     Returns the index of first occurrence of x 	my_list.index(5)
count(x)	     Returns number of times x appears          	my_list.count(2)
sort()	         Sorts list in ascending order	                my_list.sort()
reverse()	     Reverses the list	                            my_list.reverse()
copy()	         Returns a copy of the list                 	new_list = my_list.copy()
clear()	         Removes all elements	                        my_list.clear()"""

my_list = [3, 1, 4, 1, 5, 9, 2]

my_list.append(6)  # append 6 to the list
print(my_list)  

my_list.sort()  # sorts the list in ascending order
print(my_list)  

my_list.remove(1)  # removes the first 1
print(my_list)  

print(my_list.pop())  # removes and return the last element


my_list.reverse()  #returns a reversed list
print(my_list)  

"""5. Nested lists"""
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested[1][2])