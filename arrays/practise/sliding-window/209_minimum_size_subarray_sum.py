class minSubArrayLen:
  """
  Difficulty: Medium

  Given an array of positive integers nums and a positive integer target, return the minimal length
  of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

  Example 1:
  Input: target = 7, nums = [2,3,1,2,4,3]
  Output: 2
  Explanation: The subarray [4,3] has the minimal length under the problem constraint.
  """

  def minSubArrayLen(target, nums):
    minLength = float("inf") # Initialise a minLength variable.
    total = 0 # Keep track of a total sum.

    L = 0 # Left pointer

    for R in range(len(nums)): # Loop through length of nums
      total += nums[R] # Add value at R pointer to total

      while total >= target: # While the total is greater or  equal to the target.
        total -= nums[L] # Subtract the L pointer from the total
        minLength = min(minLength, R - L + 1) # Set the minLength to the min between current and difference between R and L pointers.

        L += 1 # Increment L pointer by 1.

    return 0 if minLength == float("-inf") else minLength # Return 0 if minLength has no changed from infinity.

  """
  Time complexity:
  Although there is a while loop inside the for loop, time complexity is still O(n) since the while loop only
  runs when the conditions have been met.
  """