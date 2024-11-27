"""
Optimal solution:
- Initialise the K class with k, minHeap of nums using heapify
- While len(minHeap) > k, pop from the heap using heappop
- Add function takes a value, adds to the minHeap, using heappush
- If len(minHeap) > k, pop
- Return the top value in the minHeap.
"""
import heapq

class KthLargest:
  def __init__(self, k: int, nums: list[int]):
    self.k = k
    self.minHeap = nums
    heapq.heapify(self.minHeap)

    while len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)

  def add(self, val: int) -> int:
    heapq.heappush(self.minHeap, val)

    if len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)

    return self.minHeap[0]

k = KthLargest(2, [53453,45,12,312,31,23,123,123,4234,3,4,43])