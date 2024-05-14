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