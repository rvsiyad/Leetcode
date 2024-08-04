"""
Binary trees are a similar concept to linked lists and involve nodes and pointers. Tree nodes have two nodes at most (hence the name binary tree) which
point left or right - these are called the left and right child. The first node in a binary tree is called the root node.

The values within a binary tree can be any data type which can be initialised by creating a TreeNode class
"""
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
"""
If a node does not have any children, then it is considered a leaf node. If it even has one child - left or right - it is no longer considered to be a leaf node.
There is also no cycles allowed within a tree, nodes cannot go backwards. The height of a tree can be calculated by the number of nodes connected, some text books
include the root node in the height while others do not.
"""