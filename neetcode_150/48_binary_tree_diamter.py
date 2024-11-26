"""
Optimised solution DFS:
- Create a global maxDiameter variable
- Create DFS func, passing in root
- Do DFS on right and left children, storing the returned vals
- Update global max between max itself and right length and left length added
- Return the max between the left and right lengths + 1.
- Call the DFS function with the root
- Return maxDiameter.
"""
def optimised_solution(root):
  maxDiameter = 0

  def dfs(root):
    nonlocal maxDiameter

    if not root:
      return 0

    left = dfs(root.left)
    right = dfs(root.right)
    maxDiameter = max(maxDiameter, left + right)

    return 1 + max(left, right)

  dfs(root)
  return maxDiameter