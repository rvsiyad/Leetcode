class ThreeSum:
  """
  Difficulty: Medium

  Question:
  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

  Notice that the solution set must not contain duplicate triplets.

  Example 1:

  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]

  Explanation:
  nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
  nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
  nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

  The distinct triplets are [-1,0,1] and [-1,-1,2].
  Notice that the order of the output and the order of the triplets does not matter.
  """
  def threeSum(nums):
    res = [] # Initialise an empty array to hold our result
    nums.sort() # Sort into ascending order

    for i, a in enumerate(nums):
      if i > 0 and a == nums[i - 1]: # If it is not the first index and if the value before is the same
        continue # continue to the next iteration

      L, R = i + 1, len(nums) - 1 # Set the L pointer to i + 1, and R pointer to end of array

      while L < R: # Loop while L is smaller than R
        total = a + nums[L] + nums[R] # Calculate current total

        if total > 0: # If total greater than 0, more L pointer up
          L += 1
        elif total < 0: # if total smaller than 0, more R pointer down
          R -= 1
        else:
          res.append([a, nums[L], nums[R]]) # If equal to 0, add values to res
          L += 1 # Increment L
          while nums[L] == nums[L - 1] and L < R: # Check to make sure value previously is not equal, and still in bounds
            L += 1 # If inbounds and previous and current values are equal, more to next L value.

    return res # Return the result