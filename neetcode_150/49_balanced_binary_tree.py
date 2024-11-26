"""
Optimised solution:
- Create a global balanced variable
- Create a nested function
- Check if not root, return 0
- Do DFS on left and right subtrees
- Calculate the absolute diff between left heigh and right height
- This is to see if the difference between each node is not greater than 1
- If diff greater than one, update global balanced variable to false
- Return the max height from either the left or right subtree and add one
- Call the nested function and return the balanced variable.
"""
def optimised_solution(root):
  balanced = True

  def dfs(root):
    if not root:
      return 0

    left = dfs(root.left)
    right = dfs(root.right)

    absoluteDiff = abs(left - right)

    nonlocal balanced

    if absoluteDiff > 1:
      balanced = False

    return 1 + max(right, left)

  dfs(root)
  return balanced