"""
Optimised solution:
- Create set
- Loop through nums
- If num in set, return num
- Else add to set
"""
def optimised_solution(nums):
  uniqueNumbers = set()

  for num in nums:
    if num in uniqueNumbers:
      return num

    uniqueNumbers.add(num)