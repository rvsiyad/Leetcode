"""
Brute force solution:
- Create a dict for s1 string
- Fill in s1 count via looping and incrementing
- Loop over the s2 string
- Initialise empty dict
- Loop over the length of the s2 count
- Increment s2 string in count
- Check if dicts are equal, return true
- Return false
"""
def brute_force_solution(s1, s2):
  s1Count = {}

  for i in range(len(s1)):
    s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)

  for i in range(len(s2)):
    s2Count = {}
    for j in range(i, len(s2)):
      s2Count[s2[j]] = 1 + s2Count.get(s2[j], 0)

      if s2Count == s1Count:
        return True

  return False

"""
Optimised solution:
- Create two dicts for s1, s2 counts
- Loop through len(s1), add current index to s1, s2 dicts
- Compare if dicts equal, return true
- Initialise a L pointer
- Second loop from len(s1) to len(s2)
- Remove from left and add to right for s2 dict
- If zero value at L pointer, pop from dict
- Compare equality, return true if yes
- Return false outside
"""
def optimised_solution(s1, s2):
  if len(s1) > len(s2):
    return False

  s1Count, s2Count = {}, {}

  for i in range(len(s1)):
    s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
    s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

  if s1Count == s2Count:
    return True

  L = 0

  for R in range(len(s1),len(s2)):
    s2Count[s2[R]] = 1 + s2Count.get(s2[R], 0)
    s2Count[s2[L]] -= 1

    if s2Count[s2[L]] == 0:
      del s2Count[s2[L]]

    if s2Count == s1Count:
      return True

    L += 1

  return False