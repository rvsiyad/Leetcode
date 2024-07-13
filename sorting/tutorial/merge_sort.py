"""
Merge sort works by splitting the array into halves until the subarray become of size one. From there, the sub-arrays of size one
are merged together until there are two base. The merging of the two bases is down by using two pointers, pointing at the previous
subarray there two sub-arrays originated from:
  1. [3,2] not yet reached base case so is split again ->
  2. [3] [2] The base cases have been achieved ->
  3. [] = [2,3] The two pointers determine is value at one pointer is smaller than the other.
  From which they are merged into the previous subarray.

These steps continue recursively until it reaches the final subarray which is sorted.

There are two functions needed to complete the merge sort algorithm.

1. merge() - This merges the each subarray created at each step, until it creates a sorted array:

2. mergeSort() - This is the main function behind splitting the array into it's base cases. It will not stop until the array is of base
case 1. If the array is greater than 1, it splits the array in 2 by finding the end and middle and creating pointers for them.
"""
def merge(arr, s, m, e):
  L = arr[s: m + 1]
  R = arr[m + 1 : e + 1]

  i = 0
  j = 0
  k = s

  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      arr[k] = L [i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1
  while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1

def mergeSort(arr, s, e):
  if e - s + 1 <= 1:
    return arr

  m = (s + e) // 2

  mergeSort(arr, s, m)

  mergeSort(arr, m + 1, e)

  merge(arr, s, m , e)

  return arr

arr = [2, 3, 4, 4, 5, 2, 4, 6, 81, 23, 4, 9, 9, 92, 3, 4, 4, 5, 6, 6, 7, 7, 1, 2, 4, 6, 8, 1, 23, 4, 9, 9, 9, 2, 3, 4, 4, 5, 6, 6, 7, 7, 1, 2, 4, 6, 8, 1, 23, 4, 9, 9, 9]
sorted_arr = mergeSort(arr, 0, len(arr) - 1)
print(sorted_arr)