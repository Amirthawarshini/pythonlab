# Dictonary creation
student = {
    "name": "John",
    "age": 20,
    "course": "python"
    }
# Accessing values
print(student["name"])

# adding a new key-value pair
student["grade"] = "A"

# Updating a value
student["age"] = 21

# Deleting a key-value pair
del student["course"]

print("Updated Dictionary:", student)
