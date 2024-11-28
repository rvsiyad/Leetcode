"""
Optimal solution:
- Create a new results arr
- Loop through the intervals
- If the newIntervals end time is smaller than intervals[i] start time
  - No need to merge
  - Append the interval to the result and return the remainder of the intervals array.
- If the newIntervals start time is greater than intervals[i] end time
  - No need to merge, add interval[i] to result
- In all other situations, both are overlapping, we must merge
  - This can be done by taking the min of both start times and max of both end times, and making that the newInterval
- Append the remaining newInterval if not appended within the loop
- Return the result.
"""
def optimal_solution(newInterval, intervals):
  res = []

  for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:
      res.append(newInterval)
      return res + intervals[i:]
    elif newInterval[0] > intervals[i][1]:
      res.append(intervals[i])
    else:
      newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

  res.append(newInterval)

  return res