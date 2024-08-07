"""
Difficulty: Easy

Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""
def maxDepth(root):
  def helper(root): # Create a helper function for the recursive DFS
    if not root: # If there is no root, return 0
      return 0

    left = helper(root.left) # DFS the left subtree
    right = helper(root.right) # DFS the right subtree

    return max(left, right) + 1 # Check the max depth between the two subtrees and add 1 to include the curr node

  return helper(root) # Return the helper function