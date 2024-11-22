"""
Brute force solution:
- Create a longestStreak to hold the longest streak, set to 0
- Sort the nums array
- Loop through the entire array
- Create a currentStreak variable
- Set the currentNum to nums[i]
- Loop through the rest of array
- If currentNum and the nums[j] are equal, continue
- If nums[j] != currentNum + 1, break
- If nums[j] == currentNum + 1, update currNum and streak by 1
- outside inner loop, Update longestStreak to max between curr and longest.
- return Longest
"""
def brute_force_solution_no1(nums):
  longestStreak = 0
  nums.sort()

  for i in range(len(nums)):
    currStreak = 1
    currNum = nums[i]

    for j in range(i + 1, len(nums)):
      if nums[j] == currNum:
        continue

      if nums[j] != currNum + 1:
        break
      else:
        currNum += 1
        currStreak += 1

    longestStreak = max(currStreak, longestStreak)

  return longestStreak

"""
Another brute force solution:
"""
def brute_force_solution_no2(nums):
  numSet = set(nums)
  longestStreak = 0

  for num in nums:
    currNum = num
    currStreak = 1

    while currNum + 1 in numSet:
      currNum += 1
      currStreak += 1

    longestStreak = max(currStreak, longestStreak)

  return longestStreak

"""
Similar brute force approach:
"""
def brute_force_solution_no3(nums):
  if not nums:
    return 0

  nums.sort()
  longestStreak = 0
  i = 0
  currStreak = 0
  currNum = nums[i]

  while i < len(nums):
    if currNum != nums[i]:
      currNum = nums[i]
      streak = 0

    while i < len(nums) and currNum == nums[i]:
      i += 1

    currStreak += 1
    currNum += 1
    longestStreak = max(currStreak, longestStreak)

  return longestStreak

"""
Optimised approach:
arr [1,1,2,3,4,5,100,200]

Have to think about it in human terms, how do we as humans convert this to a simpler problem.
Grouped together, check if it is the start of a sequence, if it is the length is 1.

- Create a set and pass in the arr
- Create longest_seq variable which we will update as we go.
- Loop through num in the arr
- If there is not a previous value in comparison to the current val, length = 1.
  - We look for this because as humans, if we are tasked with this,
    we would look for the smallest value first as this is the start of a seq.
- Now loop through checking if we have another accompanying value to the right,
- increment the length and the index.
- Update longest_seq
- Return longest_seq
"""
def optimal_solution(nums):
  longest_seq = 0
  numSet = set(nums)

  for num in nums:
    if (num - 1) not in numSet:
      length = 1

      while (num + length) in numSet:
        length += 1

      longest_seq = max(longest_seq, length)

  return longest_seq