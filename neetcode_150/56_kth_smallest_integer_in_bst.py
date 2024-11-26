"""
Optimal solution:
- Create an arr to hold nodes
- Create helper function
- If not root return
- Do inorder traversal to get smallest first:
  - DFS on left child
  - Append curr node
  - DFS right child
- Call the DFS function
- Return the arr[kth] element -1 for 1 indexed array.
"""
def optimal_solution(root, k):
  arr = []

  def dfs(root):
    if not root:
      return

    dfs(root.left)

    nonlocal arr
    arr.append(root.val)

    dfs(root.right)

  dfs(root)
  return arr[k - 1]