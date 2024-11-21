"""
Brute force solution:
- Check lens are equal, if not return false
- Sort both the s and t strings.
- Loop through len of s or t
- Check if value at the index are equal, if not return false.

Sorting is O(log-n) time complexity
Looping over the strings will run in n time.
"""
def brute_force_solution(s, t):
  if len(s) != len(t):
    return False

  s.sort()
  t.sort()

  for i in range(len(s)):
    if s[i] != t[i]:
      return False

  return True

"""
Optimised solution:
- Check if lens are the same, return false if not
- Create a dict for both of them
- if dicts are equal, return true, else false
"""
def optimised_solution(s, t):
  if len(s) != len(t):
    return False

  sDict = {}
  tDict = {}

  for i in range(len(s)):
    sDict[s[i]] = 1 + sDict.get(s[i], 0)
    tDict[t[i]] = 1 + tDict.get(t[i], 0)

  return True if sDict == tDict else False