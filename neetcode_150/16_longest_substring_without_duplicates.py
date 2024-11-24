"""
Brute force solution:
- Create the res variable
- Double loop over the values
- Within first loop, create a set
- Second loop check if current value in set
- If so we can break, else add the value to the set
- Outside this loop, update res to max between res and the set length.
"""
def brute_force_solution(s):
  res = 0

  for i in range(len(s)):
    charSet = set()

    for j in range(i + 1, len(s)):
      if s[j] in charSet:
        break

      charSet.add(s[j])

    res = max(res, len(charSet))

  return res

"""
Optimised solution:
- Sliding window:
- Create maxLength variable and hashmap
- Create L pointer equal to 0
- Loop through with R pointer
- Add R pointer value to hashmap
- While R pointer value is greater than 1, remove from L pointer and increment
- Update the maxLength against R - L + 1
- Return maxLength
"""
def optimised_solution(s):
  # Hashmap to hold the characters and remove from the hashmap
  # Remember to pop if hashmap value is 0
  count = {}
  longestSubstring = 0
  L = 0

  for R in range(len(s)):
    # Add value at the right pointer
    count[s[R]] = 1 + count.get(s[R], 0)
    # Check length equals R - L,

    while count[s[R]] > 1:
      # Remove from the left
      count[s[L]] -= 1

      if count[s[L]] == 0:
        del count[s[L]]

      L += 1

    longestSubstring = max(longestSubstring, R - L + 1)

  return longestSubstring