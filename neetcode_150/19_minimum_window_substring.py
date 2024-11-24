"""
Optimised solution:
- Create hashmaps for tCount and sCount
- Populate tCount with letter counts
- Create variables for:
  - res which holds the L and R pointer indexes
  - minLength, compares the lengths
  - have, incremented and decrements based on letters needed contained in sCount
  - need, the length of the tCount hashmap, what we compare have against
- Loop through R in range of s
- Add R pointer value to sCount
- Increment have if R pointer val in tCount and counts of vals are equal in both maps
- If have and need are equal
- Update the res and minlength to smallest of window size and current minLength
- Start removing values from L pointer
- If vals in hashmaps at L pointer is less in the sCount map than tCount, decrement have
- Increment L pointer
- Deconstruct start and end and use splicing to return string, else empty string if minLength is still the float("inf")
"""
def optimal_solution(s, t):
  tCount, sCount = {}, {}

  for c in t:
    tCount[c] = 1 + tCount.get(c, 0)

  res, minLength, have, need = [-1, -1], float("inf"), 0, len(tCount)

  L = 0

  for R in range(len(s)):
    sCount[s[R]] = 1 + sCount.get(s[R], 0)

    if s[R] in tCount and sCount[s[R]] == tCount[s[R]]:
      have += 1

    while have == need:
      if (R - L + 1) < minLength:
        res = [L, R]
        minLength = (R - L + 1)

      sCount[s[L]] -= 1

      if s[L] in tCount and sCount[s[L]] < tCount[s[L]]:
        have -= 1

      L += 1

  start, end = res

  return s[start:end+ 1] if minLength != float("inf") else ""