"""
Sets are similar to lists but are unordered and do not allow duplicates
use curly brackets
"""

# my_sets = {1, 2, 3, 4, 5, 1, 2}
# print(my_sets)
# print(len(my_sets))
#
# for i in my_sets:
#     print(i)
#
# my_sets.add(6)
# print(my_sets)
#
# my_sets.discard(6)
# print(my_sets)
#
# my_sets.update([7, 8, 9])
# print(my_sets)

"""
Tuples are similar to lists but are ordered
"""

# my_tuples = (1, 2, 3, 4, 5)
# print(my_tuples)
# print(len(my_tuples))
#
# for i in my_tuples:
#     print(i)

"""
Lists Assignment
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
"""
zoo = ['lion', 'tiger', 'elephant', 'zebra', 'giraffe']
zoo.pop(3)
zoo.append('hippo')
zoo.pop(0)
print(zoo)
print(zoo[0:3])
