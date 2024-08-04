"""
Binary search trees are similar to binary trees except they have they added sorted property on top. The assumption for a binary search tree is children to the left
node of a parent node are smaller than the value of the parent node while values at the right node will have a greater value than its parent node.

This is a recursive effect meaning this is the same for all children of the parents, so each node - if it not a leaf node - will have a child node with the left
nodes value being smaller and the right nodes value being greater. This will continue all the way to the root node at the top of the tree.

Binary search trees allow us to search within a sorted tree in O(log-n) time, meaning at each iteration, we are halving the number of nodes we need to search.

Since trees are a recursive data structure, the simplest way to traverse a tree is using recursion.
"""
def search(root, target): # We can create a function called search which takes in the root node and the target value
  if not root: # If there is no root i.e. the root is Null, we can return False. Meaning we have traversed the entire tree and not found the target value.
    return False

  if root.val > target: # If the root nodes value is greater than the target
    return search(root.left, target) # we search towards the left side, which has smaller values than the current node. Make sure to return!!!!
  elif root.val < target: # If the root nodes value is smaller than the target
    return search(root.right, target) # we search towards the right side, which has bigger values than the current node. Make sure to return!!!!!
  else:
    return True # Else we have found the target node and return True.

"""
Conditions 2 and 3 (root.val > target and root.val < target), is where we are making our recursive calls. The chain will continue on until the target value is found,
and once it is, each function call made before will return True. Conditions 1 and 4 are our base cases, either calling True or False if we find out target node or not.

Time complexity:
If a binary search tree is balanced, meaning there are an even number of nodes on both sides of the root node, then the worst time complexity is 0(log-n).
However in an unbalanced tree, where one side has a much greater number of nodes than the other, the time complexity is O(n) - it is as if we are traversing
a linear array.
"""