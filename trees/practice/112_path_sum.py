"""
Difficulty: Easy

Question:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
"""
def hasPathSum(root, targetSum):
  def helper(root, targetSum, total):
    if not root: # If we reach the end of end of the path and there is no route, we can return False
      return False

    total += root.val # Increment the total with the value at the current root node

    if total == targetSum and not root.left and not root.right: # If the total equals the target and there are no children left in the path, we can return True
      return True

    return helper(root.left, targetSum, total) or helper(root.right, targetSum, total) # Call the helper function again to see if the left or right paths return True

  return helper(root, targetSum, 0) # Call the helper function in the hasPathSum