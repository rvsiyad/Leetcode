"""
DFS is used to traverse an array by going to its deepest nodes first. This can be either in the left or right direction, which will
occur recursively, going as deep right as possible.

There are three ways to traverse a tree using DFS:
  - in_order traversal - This will print the nodes in order of their values
  - pre_order traversal - This will go through the nodes printing the parent node first
  - post_order traversal - This will print the left then right and lastly the parent node.

Another way to print a tree is via reverse_order, this prints the nodes in reverse order
"""
# Prints nodes in sorted order
def inorder(root):
  if not root:
    return

  inorder(root.left)
  print(root.val)
  inorder(root.right)

# Prints the parent node first before the left and right children
def pre_order(root):
  if not root:
    return

  print(root.val)
  pre_order(root.left)
  pre_order(root.right)

# Prints the parent node last
def post_order(root):
  if not root:
    return

  post_order(root.left)
  post_order(root.right)
  print(root.val)

# Prints in reverse order
def reverse_order(root):
  if not root:
    return

  reverse_order(root.right)
  reverse_order(root.left)
  print(root.val)