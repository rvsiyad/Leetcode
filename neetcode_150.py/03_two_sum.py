"""
Brute force solution:
- Double for loop over the nums array
- if nums[i] + nums[j] == target, return True
- end of func, return False
"""
def brute_force_solution(nums, target):
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

"""
Optimised solution:
- Need to return the indexes, we can use a hashmap to store the indexes
- Loop using enumerate, to get the indexes
- We can do it in one loop, first check if diff in hashmap, return the indices

- Some questions may ask for smaller index first, just use an if statement to put smaller index first.
"""
def optimised_solution(nums, target):
  num_dict = {}

  for i, num in enumerate(nums):
    diff = target - num

    if diff in num_dict:
      return [i, num_dict[diff]]
    else:
      num_dict[num] = i

