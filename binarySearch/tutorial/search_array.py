"""
Binary search is a searching algorithm that works in O(log-n) time, making it much faster than looping through an entire array.
The algorithm only works when the array in question is sorted as it relies on splitting the array in half when the target value
is higher or lower than where the middle pointer is.

Binary search returns the index at which the target value is present.
"""
def binarySearch(arr, target):
  L, R = 0, len(arr) - 1

  while L <= R:
    m = (R + L) // 2

    if target > arr[m]:
      L = m + 1
    elif target < arr[m]:
      R = m - 1
    else:
      return m

  return -1

print(binarySearch([0,1,2,3,4,5,6,7,8,9,10], 8))
