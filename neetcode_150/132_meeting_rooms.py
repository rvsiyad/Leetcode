"""
Optimal solution:
- Return True if no intervals
- Return True if intervals len() == 1
- Sort the intervals by the start times
- Create a prevEnd variable which is initialised with the end of the first interval
- Loop through all other intervals after the first [1:]
- If prevEnd > interval.start, there is an overlap, return False
- Else update the prevEnd to the interval.end
- Return True
"""
def optimal_solution(intervals):
  if not intervals:
    return True

  if len(intervals) == 1:
      return True

  intervals.sort(key=lambda x:x.start)

  prevEnd = intervals[0].end

  for interval in intervals[1:]:
      if prevEnd > interval.start:
          return False
      else:
          prevEnd = interval.end

  return True