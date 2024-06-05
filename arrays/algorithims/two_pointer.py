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

