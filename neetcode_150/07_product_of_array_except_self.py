"""
Optimal solution:
- Create the array which will hold the values from the suffix, prefix calculations
- Create a prefixVal initialised to 1.
- Loop through res
- res at current index to equal the prefixVal
- update prefix to *= nums[i]
- Create a suffixVal initialised to 1
- Loop backwards over res
- res at the current index *= suffix val
- update suffix val to be multiplied by the nums[i] value.
- return res
"""
def optimal_solution(nums):
  res = [1] * len(nums)

  prefix_val = 1
  for i in range(len(nums)):
    res[i] = prefix_val
    prefix_val *= nums[i]

  suffix_val = 1

  for i in range(len(nums) -1, -1, -1):
    res[i] *= suffix_val
    suffix_val *= nums[i]
  
  return res