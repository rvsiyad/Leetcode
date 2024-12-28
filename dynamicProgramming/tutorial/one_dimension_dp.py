"""
Dynamic programming is the optimised approach of recursion. We take a big problem and break it down into smaller problems.
DP can generally more optimised than recursion when it comes to space and time complexity.

Looking at the recursive approach to complete the fibonacci sequence, this takes O(n^2) as at each level, we make 2 more calls
of the recursive function:
"""
def bruteForce(n):
  # If we reach the base cases, we return n.
  if n <= 1:
    return n

  # Else we call the function again to return the sum of the two previous fibonacci numbers.
  return bruteForce(n - 1) + bruteForce(n - 2)
"""
Although this approach does work, with dynamic programming, we can reduce the time complexity to O(n).

Image we call the previous function with n = 5, this will make multiple recursive calls to n = 2 meaning the work previously done is being
repeated multiple times. With larger inputs, this can cause the function to work extremely slow.

DP works to avoid this repetition by using a concept called memoization, also called caching. For example, if we calculate F(3), we can store the result
in a hashmap, from which later we can retrieve if we later need to do the same computation. As a result, we can retrieve from the cache in o(1).

The memoization technique for the fibonacci sequence only differs slightly:
- Add a cache parameter to the function call, our hashmap
- A check to see if the nth fib is already in the hashmap, if so we return it.
- We add the nth fib to the hashmap and store it with the recursive calls.
- We return the cache nth value.

This way of DP is referred to as the top down approach as we traverse the tree from the top going all the way down to our base cases.
"""
def memoization(n, cache):
  # Same base case, return n if 1 or less.
  if n <= 1:
    return n

  # If n in the cache, we can return the answer in O(1) time.
  if n in cache:
    return cache[n]

  # Store nth fib in a case and call the recursive functions
  cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
  # Return the cache value for n
  return cache[n]