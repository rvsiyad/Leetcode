"""
Brute force solution:
- Create a set to hold the triple values
- Triple loop over the nums array
- If we find three values that equal to zero,
- Return them by adding to set as a tuple.
- Outside loop, return using list comprehension, converting
  tuple values into a list.
"""
def brute_force_solution(nums):
  three_sums = set()

  for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
      for k in range(j + 1, len(nums)):
        if (nums[i] + nums[j] + nums[k]) == 0:
          three_sums.add(tuple([nums[i], nums[j], nums[k]]))

  return [list(i) for i in three_sums]

"""
Optimal solution:
- Sort the array
- Loop over each num in nums
- Check if current num is equal to prev num, if so, continue to next loop.
- Do two pointer on the rest of the values
- We can optimise by skipping values that are the same as the index prev
- When a value is equal to 0, we need to update the pointers:
  - We can do this by incrementing one of the pointers until they are different from the one prev.

"""

def optimal_solution(nums):
  res = []
  nums.sort()

  for i in range(len(nums)):
    L = i + 1
    R = len(nums)

    # Since the array is sorted, if we reach values greater than 0 in the outer loop
    # the sum of the remaining values will never equal 0.
    if nums[i] > 0:
      break

    while L < R:
      threeSum = (nums[i] + nums[L] + nums[R])
      if threeSum > 0:
        R -= 1
      elif threeSum < 0:
        L += 1
      else:
        res.append([nums[i], nums[L], nums[R]])
        L += 1

        while L < R and L > 0 and nums[L] == nums[L - 1]:
          L += 1

  return res