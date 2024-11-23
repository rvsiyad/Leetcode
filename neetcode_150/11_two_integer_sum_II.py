"""
Brute force solution:
- Double for loop
- Compare i and j pointers against target
- return that value
"""
def brute_force_solution(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i + 1, j + 1]

  return []

"""
Optimised solution:
Since it is sorted in order, we can use a two pointer approach
Create a pointer for start and end, compare values and move pointer
based on difference between sum of vals and the target.
"""
def optimal_solution(nums, target):
  L = 0
  R = len(nums) - 1

  while L < R:
    current_sum = nums[L] + nums[R]

    if current_sum == target:
      return [L + 1, R + 1]
    elif current_sum < target:
      L += 1
    else:
      R -= 1

  return []