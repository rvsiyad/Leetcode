class SlidingWindowFixedSize:
  # Sliding window for a fixed window size, works by having two pointers, K length apart.

  # Here is an example question:
  # Q: Given an array, return true if there are two elements within a window of size
  # that are equal.
  def containsDuplicates(nums, k):
    window = set() # A set window allows us to only contain unique values within a window.
    L = 0 # Initialise the left pointer to index 0.

    for R in range(len(nums)): # Loop through nums array.
      if R - L + 1 > k: # If the window is greater than k, remove the left pointer value.
        window.remove(nums[L])
        L += 1 # Increment the left pointer by one.
      if nums[R] in window: # If right pointer value is in the window, return true.
        return True
      window.add(nums[R]) # Else add the value to the window.

    return False # If two same values are not in the window return false.

  print(containsDuplicates([1,2,3,4,1,2,4,5], 2))

  """
  Time complexity:
  Because we are only doing one pass over the for loop, and using a set which reads and writes in
  0(1) time, the solution is 0(n) time complexity, as we are running over the loop in its's entirety.
  """

  """
  Analysis of the problem and solution:
  When a problem mentions a "sub-array of k length" it is simple to assume we may need to utilize
  the sliding window technique. The problem may ask for different requirements, such as "Find the sum of",
  "return the indexes of" or "return the length of". All can be answered with the sliding window but may need
  to use a hashmap or another data structure.
  """

  """
  Brute Force solution:
  During an interview, it is also important to mention a brute force solution to show you understand the problem.
  """
  def bruteForceSolution(nums, k):
    for L in range(len(nums)):
      for R in range(L + 1, min(len(nums), L + k)):
        if nums[L] == nums[R]:
          return True

    return False

  print(bruteForceSolution([1,2,3,4,5,5], 2))