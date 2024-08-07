"""
Difficulty: Easy

Question:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
"""
def invertTree(root):
  def helper(root): # Create a helper function which takes the root and does DFS
    if not root: # If root is null, return None
      return None

    temp = root.left # Create a temp variable which holds the roots left node
    root.left = root.right # Assign the right node to the left node
    root.right = temp # Assign the temp to the right node

    helper(root.left) # Call recursively for the left
    helper(root.right) # Call recursively for the right

    return root # Return the root

  helper(root) # Call the helper function with the root
  return root # Return the root
