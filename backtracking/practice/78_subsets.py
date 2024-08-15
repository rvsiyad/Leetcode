"""
Difficulty: Medium

Question:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
def subsets(nums):
  res = [] # We create a result array, this is what we will return. It will be an array of arrays
  subSet = [] # The subSet array will be appended to the res array and will hold individual results

  def helper(index): # We create a helper function which will be called recursively. It is based the index as a pointer
    if index >= len(nums): # If the index is greater than the length of the nums array
      res.append(subSet.copy()) # We append out subarray since we have finished the recursive steps
      return # We return out the recursive path

    subSet.append(nums[index]) # We add the value at the index to our subset
    helper(index + 1) # Call the function again at the index up

    subSet.pop() # We remove this last added value from the subSet
    helper(index + 1) # We call the helper function again with the index incremented to the next value in the nums array

  helper(0) # We call the helper function with the starting index - index of 0
  return res # We return the res array

print(subsets([1,2,3]))
"""
Notes:
- This problem requires backtracking, which means we either add the value and call the helper function, or we remove the last added value and call the helper
  with the incremented index pointing at the next value in nums.
- It is essential we think about our edge cases and what will end the recursive steps, in this case, it is if the index is out of bounds of nums.
- When appending the subSet array to the res , we make sure to do this by using a copy of the subSet. This is because it can be manipulated and affect other paths values.
"""