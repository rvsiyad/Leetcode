class RemoveDuplicatesFromSortedArray:
  """
  Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
  The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

  Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

  - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size of nums.

  - Return k.

  Example 1:

  Input: nums = [1,1,2]
  Output: 2, nums = [1,2,_]
  Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
  It does not matter what you leave beyond the returned k (hence they are underscores).

  Example 2:

  Input: nums = [0,0,1,1,1,2,2,3,3,4]
  Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
  Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
  It does not matter what you leave beyond the returned k (hence they are underscores).
  """

  def removeDuplicates(nums):
    # Create a L pointer at index 1
    L = 1

    # Loop through nums by start at index 1. This allows us to compare against the previous value, also the first value is already unique.
    for R in range(1, len(nums)):
        if nums[R] != nums[R - 1]: # If the previous value does not equal the current value...
            nums[L] = nums[R] # Assign value at the R pointer to the L pointer.
            L += 1 # Increment the L pointer.

    return L # We can return the L pointer as it is the length of unique characters.

  """
  Time complexity:
  This solution runs in O(N) time as it has no nested loops and values are being accessed in O(1) time.
  """