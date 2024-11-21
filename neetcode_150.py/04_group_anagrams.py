"""
Brute force approach:
- Create a res [] outside the loops
- Loop over the strings in str
- Create a sortedString, takes the current string and sorts it
- Create an empty array inside the first loop
- Second loop through i, len(strs)
- Sort the str[j] string, compare if equal, add to the array
- outside second loop, add to the res array
"""
def brute_force_solution(strs):
  result = []
  visited = set()

  for i in range(len(strs)):
    if i in visited:
      continue

    arr = [strs[i]]
    sortedString = ''.join(sorted(strs[i]))

    for j in range(i + 1, len(strs)):
      if j not in visited:
        comparedStringSorted = ''.join(sorted(strs[j]))
        if sortedString == comparedStringSorted:
          arr.append(strs[j])
          visited.add(j)

    visited.add(i)
    result.append(arr)

  return result

"""
Optimised approach no.1:
- Create a defaultdict of type list
- Loop through strings in str
- Create an array of all letters from index 0 - 26, representing the number of each letter.
- Loop through the char in the str
- Each char get the order and minus it from the order of a, this will fill in the index of it
- Outside this for loop, we add to the the dict by converting the array into a tuple which is immutable, and adding the str as a value by appending.
- We can then return the dicts.values and convert it into a list.
"""
from collections import defaultdict

def optimised_solution_no1(strs):
  strings_grouped = defaultdict(list)

  for string in strs:
    count = [0] * 26

    for char in string:
      index = ord(char) - ord("a")
      count[index] += 1

    strings_grouped[tuple(count)].append(string)

  return list(strings_grouped.values())

"""
Optimised solution no2:
- Similar process to solution no1, however we use the sorted strs as the default dict key
"""
def optimised_solution_no2(strs):
  strings_grouped = defaultdict(list)

  for string in strs:
    sorted_string = ''.join(sorted(string))
    strings_grouped[sorted_string].append(string)

  return list(strings_grouped.values())

test_arr = ["cat", "rat", "mat", "tac", "atc", "tar", "tam"]

print(optimised_solution_no2(test_arr))
