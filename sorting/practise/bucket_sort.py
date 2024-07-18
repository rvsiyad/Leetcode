# Sort an array which include values ranging from 0-9
def bucketSort(arr):
  counts = [0] * 10

  for n in arr:
    counts[n] += 1

  i = 0

  for n in range(len(counts)):
    for j in range(counts[n]):
      arr[i] = n
      i += 1

  return arr

print(bucketSort([0,1,2,3,4,5,6,7,3,2,1,2,2,1,2,3,4,3,5,6,8,7,9,5,2,4,5,6,7,8,4,2,1,2,3,4,5,6,3,2]))