"""
Difficulty: Easy

Question:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
"""
class Solution:
  def isSameTree(self, p, q): # We are given a method with the roots for 2 separate binary trees - p and q
    # There are a number of checks we can use to check if a binary tree is the same.
    if not p and not q: # First we check if p and q are both null, if so we return true
        return True
    if not p or not q: # If only one of p or q is null, we return False, both must be the same bool
        return False
    if p.val != q.val: # Finally we check the values, if the values are not the same, we return False
        return False

    # We call the method again recursively to check if at any point in the left or right subtrees are different via the conditions above.
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left , q.left)