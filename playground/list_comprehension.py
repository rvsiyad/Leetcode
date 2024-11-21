"""
List comprehension is the short hand way of creating list

It can allow us to create lists based on conditions and manipulate the values within a list

Syntax:
new_list = [new_value for value in list]

Or with an added condition:
new_list = [new_value for value in list if value > 34]
"""

# Example of using list comprehension to create a matrix
rows = 4
columns = 6

bumble = True

matrix = [[0] * columns for _ in range(rows) if bumble is True]

print(matrix)