"""
Difficulty: Medium

Question:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""
def lowestCommonAncestor(root, p, q):
  if not root: # If there is no root, we return null
    return None

  if root == p or root == q: # If the root is equal to p or q, we return the root
    return root

  left = lowestCommonAncestor(root.left, p, q) # If not we search the left and right subtrees
  right = lowestCommonAncestor(root.right, p, q)

  if left and right: # If both routes have the searched for values, we return the root
    return root

  if left or right: # If only one of the roots are true, we return the true root.
    return left or right
