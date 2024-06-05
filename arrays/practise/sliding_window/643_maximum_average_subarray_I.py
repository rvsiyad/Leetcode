class MaximumAverageSubarrayI:
  """
  Difficulty: Easy

  You are given an integer array nums consisting of n elements, and an integer k.
  Find a contiguous subarray whose length is equal to k that has the maximum average
  value and return this value. Any answer with a calculation error less than 10-5 will
  be accepted.

  Example 1:
  Input: nums = [1,12,-5,-6,50,3], k = 4
  Output: 12.75000

  Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

  Example 2:
  Input: nums = [5], k = 1
  Output: 5.00000
  """

  def findMaxAverage(nums, k):
    currentSum = sum(nums[:k]) # First we initialise the currentSum to the sum of first k elements in array
    maxSum = currentSum # Assign a maxSum value to the currentSum

    L = 0 # Create left pointer

    for R in range(k, len(nums)): # Loop from k to the end of array
      currentSum += nums[R] # Add value at the right pointer
      currentSum -= nums[L] # Subtract value from the left pointer

      maxSum = max(maxSum, currentSum) # Take the max between the currentSum and the maxSum

    return maxSum / k # Return the average
