"""
Optimised solution DFS:
- Check if not root, return 0
- Create a global max_depth variable
- Create a recursive DFS function, takes root and currDepth val
- If not root, update the global max with currDepth val
- Call children with dfs func and updating the curr depth by one
- Call the dfs func with the root and 0
- Return global variable
"""
def optimised_solution_dfs(root):
  if not root:
    return 0

  max_depth = 0

  def dfs(root, curr_depth):
    nonlocal max_depth

    if not root:
      max_depth = max(max_depth, curr_depth)
      return

    dfs(root.left, curr_depth + 1)
    dfs(root.right, curr_depth + 1)

  dfs(root, 0)
  return max_depth

"""
Optimised approach using BFS:
- Check if not root, return 0
- Create a maxDepth variable
- Append root to queue
- While queue
- For loop through length of the queue
- Pop left from queue
- Add children nodes to the queue if they exist
- Outside loop but inside while, increment maxDepth by 1
- Return maxDepth
"""
from collections import deque

def optimised_solution_bfs(root):
  if not root:
    return 0

  queue = deque()
  queue.append(root)

  maxDepth = 0

  while queue:
    for i in range(len(queue)):
      node = queue.popleft()

      if node.right:
        queue.append(node.right)

      if node.left:
        queue.append(node.left)

    maxDepth += 1

  return maxDepth