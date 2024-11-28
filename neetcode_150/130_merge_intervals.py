"""
Optimal solution:
- Create a new result array
- Heapify the intervals array
- While intervals in the heap
- If the heap is only of length 1, append top heap value result, and return the result
- If length of intervals > 1, pop smallest two values
- If the meetings are not overlapping, end of first smaller than start of second
  - Append the smaller value to result
  - Add other interval into the interval heap again
- Else if intervals are overlapping, we create a new interval using the min of the start times and max of end time, add back to heap
- return res
"""
import heapq

def optimal_solution(intervals):
  heapq.heapify(intervals)

  res = []

  while intervals:
    if len(intervals) == 1:
      res.append(heapq.heappop(intervals))
      return res

    interval_one = heapq.heappop(intervals)
    interval_two = heapq.heappop(intervals)

    if interval_one[1] < interval_two[0]:
      res.append(interval_one)
      heapq.heappush(intervals, interval_two)
    elif interval_one[1] >= interval_two[0]:
      newInterval = [min(interval_one[0], interval_two[0]), max(interval_one[1], interval_two[1])]
      heapq.heappush(intervals, newInterval)

  return res