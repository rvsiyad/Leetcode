class twoPointer:
  """
  Two pointer is like the parent of the sliding window technique. The main idea for Two Pointer
  is having a L (left) and R (right) pointer, both starting at some index of the array. The starting
  points for the L and R pointer really depends on the problem at hand.

  The concept:
  - Start with a L pointer at index 0
  - R pointer at index arr.length - 1
  - Increment or decrement the R or L pointer, depending on the conditions for the given problem.
  """

  # Here is a simple example question:
  # Q: Check if an array is a palindrome:
  def isPalindrome(word):
    # First we initialise the L and R pointer to the start and end indexes
    L, R = 0, len(word) - 1

    # create a while loop, while L pointer is less than the R pointer
    while L < R:
      if word[L] != word[R]: # If the values at the indexes do not match, return False
        return False

      L += 1  # Increment the L pointer up by 1
      R -= 1 # Decrement the R pointer down by 1

    return True # Return True if conditions are not met.

  # Here is a slightly more complex example:
  # Q: Given a sorted input array, return the two indices of two elements which sums up to the target value.
  # Assume there is exactly one solution.
  def targetSum(nums, target):
    L = 0 # Set the L pointer to index 0
    R = len(nums) - 1 # Set the right pointer to last index

    while L < R: # While L pointer is smaller than R pointer
      if nums[L] + nums[R] > target: # If sum is greater than target
        R -= 1 # Decrement R pointer, as values to left of R pointer are smaller
      elif nums[L] + nums[R] < target: # If sum is smaller than target
        L += 1 # Increment L pointer, as values to the right of L pointer are bigger
      else:
        return [L, R] # If values at L and R pointer are equal, return the indices

