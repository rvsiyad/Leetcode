"""
Brute force the solution:
- Create maxArea variable
- Double loop over the heights
- currArea calculation
- compare maxArea vs currArea
- return maxArea
"""
def brute_force_solution(heights):
  max_area = 0

  for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
      curr_area = (j - i) * min(heights[i], heights[j])
      max_area = max(max_area, curr_area)

  return max_area

"""
Optimised solution:
- Two pointer approach
- Create a maxArea variable
- Create L and R pointers
- while L < R
- currArea calculation
- update maxArea
- Update pointers based on greater heights
- Update single pointer if equal
- return maxArea
"""
def optimised_solution(heights):
  maxArea = 0
  L = 0
  R = len(heights) - 1

  while L < R:
    currArea = (R - L) * min(heights[L], heights[R])
    maxArea = max(maxArea, currArea)

    if heights[R] > heights[L]:
      L += 1
    elif heights[L] > heights[R]:
      R -= 1
    else:
      R -= 1

  return maxArea