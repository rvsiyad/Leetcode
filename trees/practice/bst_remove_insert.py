def minValue(root):
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr

def remove(root, val):
  if not root:
    return None

  if val > root.val:
    root.right = remove(root.right, val)
  elif val < root.val:
    root.left = remove(root.left, val)
  else:
    if not root.right:
      return root.left
    if not root.left:
      return root.right
    else:
      minNode = minValue(root.right)
      root.val = minNode.val
      root.right = remove(root.right, minNode.val)
  return root

def insert(root, val):
  if not root:
    return TreeNode(val)  # type: ignore

  if val > root.val:
    root.right = insert(root.right, val)
  elif val < root.val:
    root.left = insert(root.left, val)
  return root
