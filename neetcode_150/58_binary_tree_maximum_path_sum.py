"""
Optimal solution:
- Create a result variable initialised with the roots value.
- Create the dfs function, passing in the root.
- If not root, we return 0
- Get the max from the left and right subtrees, making sure to max against zero. With splitting
- Return the current node val plus the max from the right and left subtrees. Without splitting.
"""
def optimal_solution(root):
  res = root.val

  def dfs(root):
    if not root:
      return 0

    leftTree = max(dfs(root.left), 0)
    rightTree = max(dfs(root.right), 0)

    res = max(res, root.val + leftTree + rightTree)

    return root.val + max(leftTree, rightTree)

  dfs(root)
  return res