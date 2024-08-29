"""
Python comes with a library called heapq which be used to create minHeap/maxHeap from lists. The process of creating a heap
is called heapify which creates a minHeap. To use minHeap to create a maxHeap, just make all values negative, meaning the smallest
value in the minHeap is the largest just negative.
"""
import heapq

nums = [1,353,4,5,-1,7,8,2]
heapq.heapify(nums) # heapify() converts a list or iterable into a heap

# Adding to a heap and maintaining the heap order, takes the list and the value being added
heapq.heappush(nums, -2)

# Removing the min value from a heap
minVal = heapq.heappop(nums) # Works similar to a stack, can be saved to a variable as well
print(nums)

# Max heap implementation
nums2 = [1,2,3,4,5,6,6,77,7,8]
# Make the numbers negative
for i in range(len(nums2)):
  nums2[i] = nums2[i] * -1

# Now heapify()
heapq.heapify(nums2)

# Return the min val and multiply by -1 to return maxVal
maxVal = heapq.heappop(nums2) * -1
print(maxVal)

"""
Time complexity:
- heapify() is a O(n) time operation
- heappop() is a O(log-n) time operation
- heappush() is a O(log-n) time operation
- Accessing the minVal is O(1).
"""