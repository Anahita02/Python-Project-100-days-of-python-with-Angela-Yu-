# Challenge: Use list comprehensions to create new lists based on existing data.
numbers = [1, 2, 3]

print("Original list:", numbers)

new_number = [num + 1 for num in numbers]

print("New list with each number incremented by 1:", new_number)

# Challenge: Use list comprehensions to create a new list of letters from a given name.
name = "Angela"

print("Original name:", name)

new_name = [letter for letter in name]

print("New name with each letter in the original case:", new_name)

# Challenge: Use list comprehensions to create a new list of numbers based on a range of values.
range(1, 5)

print("Range from 1 to 4:", list(range(1, 5)))

new_range = [num * 2 for num in range(1, 5)]

print("New list with each number in the range multiplied by 2:", new_range)

# Challenge: Use list comprehensions to create a new list of names that are shorter than 5 characters from an existing list of names.

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

print("Original list of names:", names)

new_names = [name for name in names if len(name) < 5]

print("New list with names shorter than 5 characters:", new_names)

# Challenge: Use list comprehensions to create a new list of names that are longer than 5 characters from an existing list of names, and convert those names to uppercase.

new_uppercase_names = [name.upper() for name in names if len(name) > 5]

print("New list with names longer than 5 characters in uppercase:", new_uppercase_names)