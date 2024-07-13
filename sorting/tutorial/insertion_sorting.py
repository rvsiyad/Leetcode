class InsertionSorting:
  """
  Insertion sort is the simplest sorting algorithm that works best on small data sizes.

  Take an array for example, it works by breaking the array into smaller sub-arrays and sorting them into smallest to largest.
  It starts with a subarray of size 2, compares both values, sorts them if necessary. Then compares the subarray of size 3, sorts them,
  swaps if necessary and so on ...

  Insertion sort is implemented by using two loop, a first loop using a for loop and a second using a while loop. The while loop will only
  run if the conditions are met. For instance if the value before is smaller than the current value, the while loop is not started.

  Here is the insertion algorithm:
  """
  def insertionSort(arr):
    for i in range(len(arr)):
      j = i - 1

      while j >= 0 and arr[j + 1] < arr[j]:
        temp = arr[j + 1]
        arr[j + 1] = arr[j]
        arr[j] = temp
        j -= 1

    return arr

  print(insertionSort([1,6,8,2,3,7,9,5,4]))

  """
  Analysis:
  The Insertion sort algorithm is considered a stable sorting algo. This is because it maintains the relative order of the values. It will
  not swap the values if they are equal.

  Time complexity:
  The time complexity for insertion sort is o(n^2). This is because in the worst case scenario, the array is in reverse order and requires all
  elements to be moved. This is great when the sample size is small, but when the data is large it can be very slow.
  """