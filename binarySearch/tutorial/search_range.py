"""
In some scenarios, we are not given a target value but instead a range of values. This is like a real scenario where we are asked by someone to guess a value
between 1-100. Here we can guess a value and we are told where it is the correct value, or if we are higher or lower from the target value.

In this case, we can call another function which will check for us and respond with either correct, higher or lower.
"""
def binarySearchRange(arr):
  L , R = 0, len(arr) - 1

  while L <= R:
    m = (L + R) // 2

    if isCorrect(m) > 0:
      L = m + 1
    elif isCorrect(m) < 0:
      R = m - 1
    else:
      return m

  return -1

def isCorrect(n):
  target = 34

  if n > target:
    return 1
  elif n < target:
    return -1
  else:
    return 0

"""
Time complexity:
This runs in the exact same time as previous binary searches so O(log-n)
"""