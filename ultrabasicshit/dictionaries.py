#dictionaries are objects that store key-value pairs

# creating a dictionary

users = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {'name': 'Salman', 'age': 19, 'city': 'Karachi'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
         ]



print("Original dictionary:", users)
# accessing values
print("Accessing Alice's age:", users[0]['age'])