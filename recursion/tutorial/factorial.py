class Factorial:
  """
  One Branch Recursion:

  Recursion is when a function calls itself until it reaches a certain goal. While a for loop or while loop uses iteration
  to traverse over values, a recursive function achieves this by calling itself until the base function is reached.

  Recursive function can have two parts:
    1. The base case
    2. The function calling itself with a different input.

    Here is an example recursive function using factorials - Recursively times values by itself multiplied by n - 1.
  """
  def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
      return 1

    # Recursive case: n! (n factorial) - n * (n - 1)
    return n * Factorial.factorial(n - 1)

# Once n reaches the base case of 1, all calculations now work backwards, so will return all values greater than 1.

"""
Time complexity:
As the solution requires us to loop over each value in n, the solution runs in O(n) time. This is the same as a regular
iterative approach.

Space complexity:
However, as the solution is recursive, the values on each run must be saved in memory to be recalled. As a result, the
space complexity is O(n).

Closing Notes:
Recursion will be very useful when working with trees as they can be used to perform depth-first search.
"""