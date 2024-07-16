def merge(arr, s, m, e):
  L = arr[s : m + 1]
  R = arr[m + 1 : e + 1]

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
  if (e - s + 1) <= 1:
    return arr

  m = (e + s) // 2

  mergeSort(arr, s, m)
  mergeSort(arr, m + 1, e)

  merge(arr, s, m, e)

  return arr

arr = [5,7,8,2,3,5,79,9,2,1,3,4,4,4,5,5,5,6,67,7,7,8,8,8,8,9,5645,2,2,4234,234,23,234,23,423]

print(mergeSort(arr, 0, len(arr) - 1))