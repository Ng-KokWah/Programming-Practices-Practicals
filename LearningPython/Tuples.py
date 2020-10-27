"""Tuples is a type of data structure,
which is like a container to store different values
Very similar to lists, with some differences

Unlike lists, tuples are immutable, which means that once created it cannot
be changed or modified

For the purpose of data that does not change e.g. coordinates
"""

# same as lists, the index starts from 0
coordinates = (4, 5)

# coordinates[1] = 10 this gives an error, cause it is immutable

print(coordinates[0])  # prints out the first index item

