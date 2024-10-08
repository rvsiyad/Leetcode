"""
Difficulty: Easy

Question:
You are given two binary trees root1 and root2. Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into
a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.
Note: The merging process must start from the root nodes of both trees.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""
class Solution:
  def mergeTrees(self, root1, root2):
    if not root1 and not root2:
      return None
    elif not root1 and root2:
      root = TreeNode(root2.val) # type: ignore
    elif not root2 and root1:
      root = TreeNode(root2.val) # type: ignore
    else:
      root = TreeNode(root1.val + root2.val) # type: ignore

    root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

    return root