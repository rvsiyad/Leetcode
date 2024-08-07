"""
Binary Search Tree sets and maps are interfaces that can be implemented using trees. Using a tree to implement them means we can insert, delete and search
in O(log-n) time.

Sets:
  Imagine we have a phone book with the three names 'Alice', 'Brad', 'Collin'. We could store these using a dynamic array but sets ensure we can have unique
  values in our data structure and have them sorted alphabetically.
"""
# Defining a set in python
x = set() # This defines an empty set

y = set(['foo', 'bar', 'baz', 'foo', 'qux']) # Sets can also take in iterables such as lists and remove duplicates.
print(y) # -> {'foo', 'qux', 'bar', 'baz'}

z = set(list('Roble')) # Strings can also be placed into a set by converting to a list
print(z) # -> {'R','o','b','l','e'}
"""
Maps:
  Maps on the other hand operate using a key-value pair system. If implemented via a tree it is called a 'TreeMap' and in python it is referred to as a SortedDict.
  Take the previous example, now not only can we store the names but we can map them to their phone numbers. The data structure itself is sorted via the key and as
  a result, we can map to all information associated with that key.
    - e.g. {'Alice' : 123, 'Brad' : 345, 'Collin' : 678}
"""
from sortedcontainers import SortedDict # TreeMaps or sortedDicts are imported as such.  # type: ignore

treeMap = SortedDict({'c': 3, 'a': 1, 'b': 2}) # This is how they are defined, using key - value pairing.
