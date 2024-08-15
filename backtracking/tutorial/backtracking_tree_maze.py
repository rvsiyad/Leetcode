"""
Backtracking is very similar to DFS but it operates in a brute-force approach which is to try all possible solutions and backtrack when it hits a dead-end.
For example, imagine you are trapped in a maze are trying to find a way out. We can try all possible paths until we find the correct one. If we hit a dead
end, we backtrack and try another path. This is the overarching concept behind backtracking.

The motivation behind backtracking is solving problems like trying to find a path form the root to a leaf node that does not have any 0 value nodes. If such
a path exists, we can return True else we return False.
"""
class TreeNode(): # Set up the tree node class
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def canReachLeaf(root): # Our can reach lead node class takes in the root of the tree
  if not root or root.val == 0: # If there is no root or the value of the root is 0, we can immediately return False
    return False

  if not root.right and not root.left: # If there is no right and not left child, we can return True
    return True

  if canReachLeaf(root.left): # If there is a left child, we run the canReachLeaf() function recursively for the left subtree, return True if all children return True
    return True

  if canReachLeaf(root.right): # If there is a right child, we run the canReachLeaf() function recursively for right subtree, return True if all children return True
    return True
  return False # If none of there return True, we can return False
"""
We can also use backtracking to build a path of nodes which will reach the leaf nodes without traversing a 0 val node.
This is done using backtracking by passing in an array and appending values which meet the not 0 condition. If we reach a path with a 0,
we backtrack and remove the elements added at each stage by popping from the stack.
"""
def canReachLeafPath(root, path): # We pass in the path as well to keep track of node values
  if not root and root.val == 0:
    return False

  path.append(root.val) # To keep track of the path, we can append the root values.

  if canReachLeafPath(root.left, path):
    return True

  if canReachLeafPath(root.right, path):
    return True

  path.pop() # If the recursive functions to the left and right don't return True, we remove the values from the path as there is no root in this subtree that has a none 0 path to the leaf nodes.
  return False # We return False
"""
Time and space complexity:
In the worst case, we will have to traverse all nodes in the tree to determine if there is a valid path. This means the time complexity is O(n).
The space complexity is O(h) where h is the height of the tree, we are also storing the nodes in the path stack.
"""