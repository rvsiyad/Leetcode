"""
Given a inorder and pre-order traversal for a binary tree, we can determine the original order for the tree.
"""
def buildTree(preorder, inorder):
  if not preorder or not inorder: # We check if the pre or in order arrays are empty, if they are return null
    return None

  root = TreeNode(preorder[0]) # We take the value of the node at index 0 from the preorder array and use it to create our root node.                   # type: ignore
  mid = inorder.index(preorder[0]) # We take the mid value as the index of the first node from the preorder array and find it's location in the inorder array
  root.left = buildTree(preorder[1 : mid + 1], inorder[: mid + 1]) # We use the mid value as the number of values to be split on the left and right.
  root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
  return root # We return the root.
