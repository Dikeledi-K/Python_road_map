"""1. Dictionary basic"""

# Creating dictionary- defined using {} with key: value pairs
student = {
    "name" : "Dikeledi",
    "age" : 25,
    "City" : "Johannesburg"
}

print(student)

# Accessing values - Use keys to access values
print(student["name"])

"""2. Dictionary Operations"""

# Adding and Updating elements
student["age"] = 30 # Update value
student["grade"] = "A" # Add new key-value pair

print(student)

# Removing elements
del student["City"]    # Using del
print(student)

grade = student.pop("grade") # Using pop()
print(grade)
print(student)

student.popitem() # Using popitem() removes last item
print(student)
