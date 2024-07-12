class ClimbingStairs:
  """
  Two Branch Recursion:

  A more interesting approach to recursion is via the two branch method. For this we will use the fibonacci sequence to visualize how it works.
  The fibonacci sequence is where the nth number (greater than 0), is the sum of both previous numbers. As a result, if we think about it as a
  formula - f(n) = f(n - 1) + f(n - 2). This is a recursive function, so will call the function until we reach the base case of 0 or 1.
  """

  # Recursive implementation to calculate the n-th Fibonacci number
  def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return ClimbingStairs.fibonacci(n - 1) + ClimbingStairs.fibonacci(n - 2)

  print(fibonacci(5))

  # This is a fibonacci sequence using no recursive technique.
  def climbStairs(n):
    one, two = 1, 1

    for i in range(n - 1):
      temp = one
      one = one + two
      two = temp

    return one

  print(climbStairs(5))