"""
Sometimes for binary search problems, we are given a array that is sorted but has been split into two and rearranged.
This can now be imagined to be two different sorted arrays that we must find the target within.
"""
def searchRotatedSortedArray(nums, target):
  L, R = 0, len(nums) - 1 # Create two pointers for the Left and Right of the array

  while L <= R: # Loop through the array while L is smaller than R.
    mid = (L + R) // 2 # Find the middle of the array on each loop.

    if target == nums[mid]: # If the middle value equals target, return the middle index.
      return mid

    if nums[L] <= nums[mid]: # If the value at the left is smaller/equal to the value at the mid, it means we are in the same sorted array, so we search the left side.
      if target > nums[mid]: # If the target is greater than the value at the middle (the largest value on the left side), we search the right side.
        L = mid + 1
      elif target < nums[L]: # If the target is smaller than the value at the left (the smallest value on the left side), we search on the right side.
        L = mid + 1
      else:
        R = mid - 1 # If the target passes both checks, we search the left, and can reduce our Right side.
    else: # If the value on the left is greater than the mid value, we are on the right sided portion of the array, so start searching the right side.
      if target < nums[mid]: # If the target is smaller than the smallest value on the right side, we abandon the right side.
        R = mid - 1
      elif target > nums[R]: # If the target is greater than our greatest value on the right, we also reduce our right side.
        R = mid - 1
      else:
        L = mid + 1 # Else we will find out target on the right side, so we reduce our search and remove the left side.

  return -1 # If our target is not found, we return -1.