"""
Optimal solution using minHeap:
- Heapify intervals
- Create result
- Loop through intervals
- If len of intervals is 1, return result
- Pop two smallest interval times
- If smaller intervals end time is smaller or equal to other intervals start time
  - Add back the second interval into heap
- Else we add the interval with the smaller end time back into the heap, less likely to overlap.
- Also increment result up by 1
- Return result.
"""
import heapq

class Solution:
  def removeOverlapping(self, intervals: list[list[int]]) -> int:
    heapq.heapify(intervals)
    result = 0

    while intervals:
      if len(intervals) == 1:
        return result

      intervalOne = heapq.heappop(intervals)
      intervalTwo = heapq.heappop(intervals)

      if intervalOne[1] <= intervalTwo[0]:
        heapq.heappush(intervals, intervalTwo)
      else:
        if intervalOne[1] < intervalTwo[1]:
          heapq.heappush(intervals, intervalOne)
        else:
          heapq.heappush(intervals, intervalTwo)
        result += 1

    return result

"""
Optimal solution using greedy:
- Create result variable
- Sort the intervals by the start times
- Create a prevEnd variable which is initialised with the end of the first interval
- Loop through all other intervals after the first [1:]
- If prevEnd > start time, there is an overlap, increment the result and prevEnd is now the min of the two ends, as we don't want more overlaps
- Else update the prevEnd to the interval.end
- Return result
"""
def removeOverlappingIntervals(intervals : list[list[int]]) -> int:
	intervals.sort()
	result = 0

	prevEnd = intervals[0][1]

	for start, end in intervals[1:]:
		if prevEnd <= start:
			prevEnd = end
		else:
			result += 1
			prevEnd = min(prevEnd, end)

	return result
