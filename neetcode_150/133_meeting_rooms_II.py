"""
Optimal solution:
- Create two arrays for the start and end times for intervals and sort them
- Create a pointer for both the start and end of both arrays
- While there are start times
- Compare if the start time is smaller than the end time, if so, increment count and s pointer
- Else we decrement count and increment e pointer
- Update res to max of count and itself.
"""
class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

def optimal_solution(intervals: list[Interval]):
  start = sorted([i.start for i in intervals])
  end = sorted([i.end for i in intervals])

  s = 0
  e = 0

  count = 0
  res = 0

  while s < len(start):
    if start[s] < end[e]:
      count += 1
      s += 1
    else:
      e += 1
      count -= 1

    res = max(res, count)

  return res