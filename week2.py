# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Print my_list after appending the elements
print(f"my_list after appending elements: {my_list}")

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
# Print my_list after adding 15 in the second position
print(f"my_list after inserting 15 at index 1: {my_list}")

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
# Print my_list after extending it with another list
print(f"my_list after extending with [50, 60, 70]: {my_list}")

# Remove the last element from my_list
my_list.pop()
# Print my_list after removing the last element
print(f"my_list after removing the last element: {my_list}")

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)

print(f"The index of 30 in my_list is: {index_of_30}")
