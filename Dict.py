# Create a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(my_dict)
# Add a new item
my_dict['email'] = 'alice@example.com'

# Change the age
my_dict['age'] = 31

# Remove the city
del my_dict['city']

# Print the entire dictionary
print("Final Dictionary:")
print(my_dict)

# Print specific items
print("Name:", my_dict['name'])

# Print all items
print("All items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
