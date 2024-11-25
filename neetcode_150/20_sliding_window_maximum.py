"""
Brute force solution:
- Create a res and queue
- Loop through first k elements
- Append to the queue
- Append max(queue) to res
- Loop from k to end of nums
- Append current index value to queue
- Popleft value from queue
- Append max(queue) val to res
- Return res
"""
from collections import deque

def optimal_solution(nums, k):
  queue = deque()
  res = []

  for i in range(k):
    queue.append(nums[i])

  res.append(max(queue))

  for i in range(k, len(nums)):
    queue.append(nums[i])
    queue.popleft()

    res.append(max(queue))

  return res

"""
Optimised solution:
- Create the res array and queue
- Create R and L pointers, both initialised to 0
- While loop through nums using R pointer
- Inner while loop to pop from queue:
  - Pop from queue is there are values in the queue
  - And if the nums value using the top index in the queue is smaller than current R pointer val
- Outside this while loop, append the new R pointer
- If L pointer is greater than the first index in the queue, we pop left
- If R pointer + 1 is greater than K window size, we append to the res using the leftmost index, using the index in  nums, increment L pointer
- Increment R pointer
- Return res
"""
def optimised_solution(nums, k):
  res, queue = [], deque()
  L = 0

  for R in range(len(nums)):
    while queue and nums[queue[-1]] < nums[R]:
      queue.pop()

    queue.append(R)

    if L > queue[0]:
      queue.popleft()

    if (R + 1) > k:
      res.append(nums[queue[0]])
      L += 1

  return res