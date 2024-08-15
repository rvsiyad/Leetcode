"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
"""
def combinationSum(candidates, target): # We are given an array of candidates and a target, we want to return all combinations of candidates which equal the target
  res = [] # We create an array for the result, it will be an array of arrays
  subSet = [] # We create a subSet array, going to hold our manipulated subarray

  def helper(index, total): # This helper will complete our backtracking recursive steps. We pass in a index pointer and a total to keep track of the current sum.
    if total == target: # If the total equals the target
      res.append(subSet.copy()) # We append the subset as a copy to the result array
      return # We can return out of this pathway

    if index >= len(candidates) or total > target: # If the index is out of bounds or the total is greater than the target
      return # We can return since we will not find a subSet equal to the target down this path

    subSet.append(candidates[index]) # We append the candidates at the index to the subSet
    helper(index, total + candidates[index]) # Since we are including duplicates that can equal the target, we do not move the index up the candidates array
    # We also add the value at the index of the candidates array to the running total

    subSet.pop() # Since we are backtracking, we remove the last added value,
    helper(index + 1, total) # And we increment out index by one up the candidates array, and leave the total as is.

  helper(0, 0) # We call the helper function with the starting index of 0 and a total of 0
  return res # We can return our results array

print(combinationSum([2,3,6,7], 30))
"""
Notes:
- The outline is similar to the previous subset problem except we are still including duplicates which may add up to the target.
- The main steps with these problems is finding the base case under which the recursive steps should end. In this case it is not only the face
  the index can be out of bounds, but also the fact the sum of the subSet could be greater than the target.
"""