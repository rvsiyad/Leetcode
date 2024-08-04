class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
"""
Inserting and removing nodes within a binary search tree has a better time complexity than inserting and removing from a binary sorted array.
This is mainly because we are dealing with pointers which do not require us to move all adjacent elements like is necessary when removing from
the middle of an array. This allows us to insert and remove nodes in O(log-n) time.

This however does assume that the tree is balanced. else it becomes a O(n) operation.

If we wish to insert a new node into a BST we first have to traverse the BST to find the correct position and then insert the node.
"""
def insert(root, val): # We call insert function which takes in the root and a value to be inserted
  if not root: # Check if there is a node or not,
    return TreeNode(val) # if null we return a new TreeNode, either at the right or left which is being called recursively to point at the new node

  # Next we check if we need to go left or right
  if val > root.val: # If the new nodes value is greater than the current node, we call insert on the right node
    root.right = insert(root.right, val)
  elif val < root.val: # If the new nodes value is smaller than the current node, we call insert on the left node
    root.left = insert(root.left, val)
  else:
    return root # Finally, if the value is equal to the root node, we return the node.
"""
When removing nodes from a BST there are two cases that must be considered:
  - Case 1: The node we are removing has 0 or 1 child
  - Case 2: The node we are removing has 2 children.

If we are removing a node with 0 children, the parent of the node we wish to delete now points to Null. If we wish to remove a node with one child node, the parent
node of the node we wish to remove will point to the child of the removed node.

If we are removing a node with 2 children, we look for the in-order successor. The in-order successor is the left-most node in the right subtree of the target node.
"""
# First we create a function to find the minimum node
def minValueNode(root):
  curr = root # We create a curr variable which holds our root node
  while curr and curr.left: # Loop through while curr is not null and there is a curr.left
    curr = curr.left # reassign curr to its left node - curr.left
  return curr # When the loop breaks, because there is no left node or the root is null, we return curr

# Next we create our remove function which uses the minValueNode() function we created
def remove(root, val): # We pass in the root node and the val we wish to remove.
  if not root: # If the root node is null, we return None
    return None

  if val > root.val: # If the target val is greater than the root.val, we search towards the right subtree
    root.right = remove(root.right, val)
  elif val < root.val:
    root.left = remove(root.left, val) # If the target val is smaller than the root.val, we search towards the left subtree
  else: # Else we have found our target node and must now check to see if the node has children or not. Having 0-1 children can be dealt the same, unlike 2 children
    if not root.left: # If there is not a left child for the target node, we return the right child
      return root.right
    elif not root.right: # Else if there is no right child for the target node, we return the left child
      return root.left
    else: # Else our target node has two children, in which case we must replace it with its in order successor
      minNode = minValueNode(root.right) # We find our min node in the right subtree of our target node
      root.val = minNode.val # We reassign the target nodes value with the minNodes value
      root.right = remove(root.right, minNode.val) # We then remove the duplicate minNode value.
  return root # We return the root node each time the remove() function is called recursively.
"""
Time complexity:
The time complexity of inserting and removing from a BST is proportional to the height of the tree. In a balanced tree this would be similar to binary search on
an array and will run in O(log-n) time. However, in an unbalanced tree, this can run in O(n) time.
"""