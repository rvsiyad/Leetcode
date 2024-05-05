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
