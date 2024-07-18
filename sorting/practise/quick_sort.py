def quickSort(arr, s, e):
  if e - s + 1 <= 1:
    return arr

  pivot = arr[e]
  left = s

  for i in range(s, e):
    if arr[i] < pivot:
      temp = arr[left]
      arr[left] = arr[i]
      arr[i] = temp
      left += 1

  arr[e] = arr[left]
  arr[left] = pivot

  quickSort(arr, s, left - 1)
  quickSort(arr, left + 1, e)

  return arr

arr = [8,9,7,6,8,5,3,1,2,3,8,9,0,1,2,3,4]

print(quickSort(arr, 0, len(arr) - 1))