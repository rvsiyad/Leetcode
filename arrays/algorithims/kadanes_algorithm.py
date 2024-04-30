class KadanesAlgorithm:

  # Kadane's algorithm is used to calculate the maximum sum of a sub-array.
  def kadanes (nums):
    maxSum = nums[0] # First we initialise a max sum variable to the first value in the array.
    curSum = 0 # We then initialise a current sum variable to 0.

    # We then loop over the array.
    for n in nums:
      # CurSum is updated each iteration to the max between itself and 0.
      # This is done as a negative curSum will not increase the maxSum.
      # As a result, the sub-array should continue with a renewed the curSum.
      curSum = max(curSum, 0)

      curSum += n # Each iteration, n is added to the curSum.
      maxSum = max(curSum, maxSum) # The max between the curSum and the maxSum is assigned to be the new max.

    return maxSum # Return the max value of the sub-array.

  testArray = [1, -6, 7, 8, -2 , -4, 9]

  maxSubArrayValue = kadanes(testArray)

  print(maxSubArrayValue)