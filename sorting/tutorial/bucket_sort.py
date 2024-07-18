"""
Bucket sort is a unique algorithm which works much better than the other sorting algorithms in O(n) time.

The idea behind it is when we have an array which has a fixed number of values (range between 0-2 etc), we can store it's occurrences in a
separate array - referred to as a bucket. After this we can loop through the bucket and add to the original array, looping through the number of
occurrences.
"""

def bucketSort(arr):
  # Assuming we have an array which only contains a inclusive and specific number of known elements, e.g. 0,1,2
  counts = [0,0,0]

  # Count the quantity of each val in the arr
  for n in arr:
    counts[n] += 1

  # Fill in each bucket in the original array
  i = 0
  for n in range(len(counts)):
    for j in range(counts[n]):
      arr[i] = n
      i += 1

  return arr

print(bucketSort([1,2,1,2,1,2,1,2,1,1,2,0,0,0,0,0,1,2]))
