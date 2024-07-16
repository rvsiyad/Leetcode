def insertionSort(arr):
  for i in range(len(arr)):
    j = i - 1

    while j >= 0 and arr[j + 1] < arr[j]:
      temp = arr[j + 1]
      arr[j + 1] = arr[j]
      arr[j] = temp
      j -= 1

  return arr

print(insertionSort([6,3,2,6,8,9,7,4,3,2,1,3,2]))