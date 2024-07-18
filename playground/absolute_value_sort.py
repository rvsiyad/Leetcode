def merge(arr, s, m, e):
  L = arr[s : m + 1]
  R = arr[m + 1 : e + 1]

  i = 0
  j = 0
  k = s

  while i < len(L) and j < len(R):
    if abs(L[i]) == abs(R[j]):
      if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
    elif abs(L[i]) < abs(R[j]):
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

def abSort(arr):
  return mergeSort(arr, 0, len(arr) - 1)

print(abSort([2,-7,-2,-2,0,9]))