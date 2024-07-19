# Quick sort
def quickSort(arr, s, e):
  if e - s + 1 <= 1:
    return arr

  pivot = arr[e]
  left = s

  for i in range(s, e):
    if arr[i] < pivot:
      temp = arr[i]
      arr[i] = arr[left]
      arr[left] = temp
      left += 1

  arr[e] = arr[left]
  arr[left] = pivot

  quickSort(arr, s, left - 1)
  quickSort(arr, left + 1, e)

  return arr

# Bucket sort
# Arr values range between 0-5
def bucketSort(arr):
  counts = [0]*6

  for n in arr:
    counts[n] += 1

  i = 0

  for n in range(len(counts)):
    for j in range(counts[n]):
      arr[i] = n
      i += 1

  return arr

# Merge sort
def merge(arr, s, m, e):
  L = arr[s : m + 1]
  R = arr[m + 1: e + 1]

  i = 0
  j = 0
  k = s

  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      arr[k] = L[i]
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

  merge(arr, s, m, e)

  return arr

# Insertion sort
def insertionSort(arr):
  for i in range(len(arr)):
    j = i - 1

    while j >= 0 and arr[j + 1] < arr[j]:
      temp = arr[j]
      arr[j] = arr[j + 1]
      arr[j + 1] = temp
      j -= 1

  return arr

print(insertionSort([645,645,6,456,45,234,234,23,42,34,23,42,342,5,34,5]))