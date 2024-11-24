"""
Prefix-Postfix solution:
- Create a prefix for all the max heights to the left of each height
- Create a postfix array for all max heights to the right of each height
- For each value in the index of the post and prefix array, compare to find min and then minus the current height
- Only add positive values to waterCollected variable
- Return water_collected

O(n) time complexity but O(n) space needed.
"""
def prefix_postfix_solution(height):
  prefix = [0] * len(height)

  maxHeightLeft = 0
  # Prefix
  for i in range(len(height)):
    prefix[i] = maxHeightLeft
    maxHeightLeft = max(maxHeightLeft, height[i])

  # Postfix
  maxHeightRight = 0
  postfix = [0] * len(height)

  for i in range(len(height) -1, -1, -1):
    postfix[i] = maxHeightRight
    maxHeightRight = max(maxHeightRight, height[i])

  maxAreaOfWater = 0
  # pick min val for both and take maxAreaOfWater
  for i in range(len(height)):
    minHeight = min(prefix[i], postfix[i])
    water_can_hold = minHeight - height[i]

    if water_can_hold > 0:
      maxAreaOfWater += water_can_hold

  return maxAreaOfWater
"""
Two pointer solution:
- Create two pointer for each end
- Create a leftMax and rightMax, holding the values at each pointer
- While L smaller than R
- Compare which heigh is smaller
- If leftMax smaller than right
  - Increment L
  - Update leftMax
  - Calculated water collected by leftMax minus height[i]
- Do same for right
"""
def two_pointer_solution(height):
  water_trapped = 0
  L = 0
  R = len(height) - 1

  left_max, right_max = height[L], height[R]

  while L < R:
    if left_max < right_max:
      L += 1
      water_in_area = left_max - height[L]
      if water_in_area > 0:
        water_trapped += water_in_area

      left_max = max(left_max, height[L])

    else:
      R -= 1
      water_in_area = right_max - height[R]
      if water_in_area > 0:
        water_trapped += water_in_area
      right_max = max(right_max, height[R])

  return water_trapped

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(prefix_postfix_solution(height))
print(two_pointer_solution(height))