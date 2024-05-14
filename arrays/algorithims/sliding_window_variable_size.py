class SlidingWindowVariableSize:
  # Previously, we looked at the sliding window technique with a fixed sized window.
  # The sliding window technique becomes more useful when used when the window size is variable.

  # Here is a simple example question:
  # Q: Find the length of the longest subarray, with the same value in each position.
  def longestSubarray(nums):
    length = 0 # First a length variable.
    L = 0 # Then we initialise the left pointer.

    # We then loop through the array at index R
    for R in range(len(nums)):
      if nums[L] != nums[R]: # We check if the value at the left and right pointers are not equal
        L = R # If they are not the same, we move the left pointer to the right pointers index.
      length = max(length, R - L + 1) # The maximum between the current length and the window is reset to the length.

    return length # We return the longest length.

  # More complicated example:
  # Q: Find the minimum length subarray, where the sum is greater or equal to the target.
  # Assume all values are positive.
  def shortestSubarray(nums, target):
    L, total = 0,0 # We create a L pointer and total sum variable
    length = float("inf") # We set a length variable to inf just to make sure we find a minimum.

    # We loop through the array
    for R in range(len(nums)):
      # We set the total to add each value at index R to the sum.
      total += nums[R]

      # While R is greater or equal to the target, we set the length to the min between the current length and
      # the difference between the L and R pointers.
      while total >= target:
        length = min(length, R - L + 1)
        total -= nums[L] # Minus the left pointer from the total
        L += 1 # Increment the L pointer by 1

    return 0 if length == float("inf") else length # Return 0 if length is "infinity", or length if it has been changed.

  """
  Time complexity:
  The beauty of this technique is that is bring the time complexity down to O(n) time. This is possible even with a
  while loop sitting within the for loop. However, because of the condition set, the while loop does not run for each iteration
  of the for loop. The while loop is not iterating n times, but rather n times in total.

  """