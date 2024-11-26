"""
Optimised solution DFS:
- Create a helper function that reverses nodes
- If not root, return none
- Swap the nodes left and right child around
- Call the function again on the nodes children
- Call the helper function and return the root.
"""
def optimal_solution_no1(root):
  def invertNodes(root):
    if not root:
      return None

    root.left, root.right = root.right, root.left

    invertNodes(root.left)
    invertNodes(root.right)

  invertNodes(root)
  return root


"""
Optimised solution BFS:

"""
from collections import deque

def optimal_solution_no2(root):
  if not root:
    return None

  queue = deque()

  queue.append(root)

  while queue:
    for i in range(len(queue)):
      node = queue.popleft()

      node.left, node.right = node.right, node.left

      if node.left:
        queue.append(node.left)

      if node.right:
        queue.append(node.right)

  return root