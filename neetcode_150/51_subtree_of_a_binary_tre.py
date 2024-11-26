"""
Optimised solution:
- If there is no subRoot, return True
- If there is a subRoot and no root, return False
- Call helper function to see if sameTree:
  - Check if there is not a root and not a subRoot, return True
  - If either is present without the other, return False
  - If both present and values are equal, recursive call function with right and left nodes
  - Else return False
- Back in original func, call recursively with right child and original subRoot, and left child and original subRoot
"""
def optimised_solution(root, subRoot):
  if not subRoot:
    return True

  if not root:
      return False

  if isSameTree(root, subRoot):
      return True

  return optimised_solution(root.right, subRoot) or optimised_solution(root.left, subRoot)

def isSameTree(root, subRoot):
  if (not root and not subRoot):
      return True

  if subRoot and root and subRoot.val == root.val:
    return isSameTree(root.right, subRoot.right) and isSameTree(root.left, subRoot.left)

  return False