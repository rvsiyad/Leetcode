"""
Brute force solution:
- Iterate over the array using a nested for loop
- compare i against j, if they are equal, return true
- end of func, return false
"""

def brute_force_solution(nums):
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if nums[i] == nums[j]:
        return True

  return False

"""
Optimised O(n) time solution:
- Create a set
- If num in set, return true
- else add to set
- end of func, return false
"""
def optimised_solution(nums):
  nums_seen = set()

  for num in nums:
    if num in nums_seen:
      return True
    else:
      nums_seen.add(num)

  return False