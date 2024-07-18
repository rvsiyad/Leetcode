"""
Quick sort works by picking an index, using that value as the pivot value and partitioning the array into two sides where everything on the left is less than or
equal to the pivot value and everything on the right is greater than the pivot value.

The pivot value within merge sort can also be optimized by picking different pivot values. Some implementations call to pick the first index, some the middle, and
other the median between the first, middle and last indexes. Most examples stick with just using the last index as the pivot value.

The sorting occurs in place, which means it does not create any extra space - unlike with merge sort.
"""
def quickSort(arr, s, e): # Quick sort takes the arr, the start and end indexes.
  if e - s + 1 <= 1: # If the length of the array is less than or equal to 1, we have reached the base case, no sorting need so return the array.
    return arr

  pivot = arr[e] # Set the pivot value to the value at the end of the array
  left = s # Create a left pointer as the start of the array

  # Now partition all elements smaller than the pivot to the left.
  for i in range(s, e):
    if arr[i] < pivot: # If the value at i is smaller than the pivot, swap places with the left pointer.
      temp = arr[i]
      arr[i] = arr[left]
      arr[left] = temp
      left += 1

  # Swap value at the pivot with the left pointer, in between the two sides of the partitions:
  arr[e] = arr[left]
  arr[left] = pivot

  # Call Quick sort for the left and right sides, which continue the partitions and call quick sort recursively until the base case is met.
  quickSort(arr, s, left - 1) # Quick sort from start to just before the pivot point
  quickSort(arr, left + 1, e) # Quick sort from after the pivot point to the end of the array

  return arr

"""
Time complexity:
It is generally agreed that quick sorts time complexity is O(n log-n), however in the worst case scenario - where an array is sorted - the time complexity is O(n^2)

Stability:
Quick sort is not a stable algorithm as there is exchanging of adjacent elements.
"""