class RemoveDuplicatesFromSortedSubArrayII:
  """
  Difficulty: Medium

  Question:
  Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
  The relative order of the elements should be kept the same.

  Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
  More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
  It does not matter what you leave beyond the first k elements.

  Return k after placing the final result in the first k slots of nums.

  Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

  Example:
  Input: nums = [1,1,1,2,2,3]
  Output: 5, nums = [1,1,2,2,3,_]
  Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
  It does not matter what you leave beyond the returned k (hence they are underscores).
  """

  def removeDuplicates(nums):
    L = 1 # We initialise a L pointer at index 1. We do this as the first index(0) will always be unique, since it is the first value. Also allows us to compare the index[i] against index[i - 1]
    count = 1 # We initialise a count to 1 since there will be at least 1 occurrence of each number in the array.

    for R in range(1, len(nums)):
      if nums[R] == nums[R - 1]:
        count += 1
      else:
        count = 1

      if count <= 2:
        nums[L] = nums[R]
        L += 1

    return L

  print(removeDuplicates([1,1,1,1,2,3,4,5,5,5,5,5]))
