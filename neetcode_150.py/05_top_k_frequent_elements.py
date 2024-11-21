"""
Brute force approach using sort:
- Create a dict
- count the occurrences of each numbers
- Create another array
- Go through the items in the dict
- Add to the array an array of the [count, num]
- sort the array
- for i in range(k):
- keep popping off the highest value and append to res array
- return res
"""
def brute_force_approach(nums, k):
  count = {}

  for num in nums:
    count[num] = 1 + count.get(num, 0)

  arr = []

  for num, count in count.items():
    arr.append([count, num])

  arr.sort()

  res = []

  for i in range(k):
    num = arr.pop()
    res.append(num[1])

  return res

nums = [1,2,2,3,3,3]
k = 2

print(brute_force_approach(nums, k))
"""
Similar approach using heap:
- Create a dict
- count the occurrences of each numbers
- Create a heap initialised using an array
- ITS MORE EFFICIENT TO PUSH TO HEAP THAN TO HEAPIFY - O(log-n) for push, O(n) for heapify
- Loop through the items in dict
- Push to heap, order as (count, num)
- If greater than k, pop from the heap, the max values will remain at the bottom
- After we can pop from the heap, range of k, add to res array and return
"""
from collections import Counter
import heapq

def sub_optimal_using_heap(nums, k):
  counter = Counter(nums)

  heap = []

  for num, count in counter.items():
    heapq.heappush(heap, (count, num))

    if len(heap) > k:
      heapq.heappop(heap)
  res = []
  while heap:
    res.append(heapq.heappop(heap)[1])

  return res

"""
Most optimal solution using bucket sort:
- Create a dict to count num occurrences
- Create an array of arrays using list comprehension, that is the length of the arr
  - This is the most frequent a value can occur
  - This array of arrays will map the count by index to the values with that count
  - e.g. nums = [1,1,1,5,5,7,3]  bucketSort = [[], [7,3], [5], [1], [], [], []]. 7 and 3 occur once, 5 twice and 1 three times.
  - We use the counter to append the numbers at the count index
  - Loop backwards over the freq array
  - If the [] is populated, append val to res []
  - If len(res) == K, return res
"""
def optimal_solution (nums, k):
  counter = Counter(nums)
  freq_bucket = [[] for i in range(len(nums) + 1)]

  for num, count in counter.items():
    freq_bucket[count].append(num)

  res = []

  for i in range(len(freq_bucket) - 1, 0, -1):
    while freq_bucket[i]:
      res.append(freq_bucket[i].pop())

      if len(res) == k:
        return res

