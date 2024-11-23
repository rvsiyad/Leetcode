"""
O(n) space and O(n) time solution:
Create newString without the spaces, compare current against reversed.
"""
def unoptimised_solution(s):
  newString = ""

  for c in s:
    if c.isalnum():
      newString += c.lower()

  return newString == newString[::-1]

"""
O(1) space and O(n) time solution:
- Use a two pointer approach to iterate from both sides
- Check if val at pointer is alphanumerical and convert to lower to compare
"""
def optimised_solution(s):
  L = 0
  R = len(s) - 1

  while L < R:
    while not s[L].isalnum() and L < R:
      L += 1

    while not s[R].isalnum() and L < R:
      R -= 1

    if s[L].lower() != s[R].lower():
      return False

    L += 1
    R -= 1

  return True