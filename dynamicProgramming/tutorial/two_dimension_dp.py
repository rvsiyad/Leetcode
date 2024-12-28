"""
Two dimensional dynamic programming is when the result relies on two sub-problems. This requires a more intuitive approach
in comparison to one dimensional DP. They also can store/cache two different ways. 1-DP stores a single list of various elements of
the same data type, while 2-DP stores an array of various arrays.

Take the following matrix for example, where we are tasked with finding all paths from the top left to the bottom right, only being
allowed to more down or to the right. This problem implies we can only go out of bounds if we go too far to the right or too far down.

    0   1   2   3
0   0   0   0   0
1   0   0   0   0
2   0   0   0   0
3   0   0   0   0

Brute force:
- We would check if we are out of bounds, if we are, we return 0.
- We check if we reached the desired indexes, then we return 1. In this case the bottom right index.
- We call the recursive function twice, returning the value returned from going down, added to the value of going right.
"""
def bruteForce(r, c, cols, rows):
  # Check for base case, out of bounds
  if r >= rows or c >= cols:
    return 0

  # Check for base case, reached desired destination
  if r == rows -1 and c == cols - 1:
    return 1

  # Return values from the right and below
  return (bruteForce(r, c + 1, cols, rows) + bruteForce(r + 1, c, cols, rows))
"""
As previously discussed with most problems before adding dynamic programming, this requires we calculate the paths multiple times. For small inputs, this
may not be a problem, but for a larger matrix, this can significantly slow down performance. The BF approach is O(2^n+m).

To make this solution more optimised, we can add memoization to return previously calculated paths. This is very similar to the previous approach but ends
up saving significant time when running meaning a time complexity of O(n).
"""
def memoization(r, c, cols, rows, cache):
  # Check for base case, out of bounds
  if r >= rows or c >= cols:
    return 0

  # Check for base case, reached desired destination
  if r == rows - 1 and c == cols - 1:
    return 1

  # Check for base case, value stored in cache
  if (r, c) in cache:
    return cache[(r, c)]

  # If not in cache, add to cache with recursive calls to right and downwards
  cache[(r, c)] = (memoization(r + 1, c, rows, cols, cache) + memoization(r, c + 1, rows, cols, cache))

  # Return the cache value
  return cache[(r, c)]
