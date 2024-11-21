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

    for j in range(i, len(strs)):
      if j not in visited:
        comparedStringSorted = ''.join(sorted(strs[j]))
        if sortedString == comparedStringSorted:
          arr.append(strs[j])
          visited.add(j)

    result.append(arr)

  return result

"""
Optimised approach:
- Create a dict
- Loop through strs
- 
"""