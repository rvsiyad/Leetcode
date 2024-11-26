"""
Optimised solution BFS:
- Conditions for checks if p and q exist
- Conditions for if they don't exist
- While loop and for loop through queue
- Pop from both queue and compare
- Append children if they exist based on conditions.
- Return if both queues are empty
"""
from collections import deque

def optimised_solution_bfs(p, q):
  if not p and not q:
    return True

  if (p and not q) or (q and not p):
    return False

  p_queue = deque()
  q_queue = deque()

  p_queue.append(p)
  q_queue.append(q)

  while p_queue and q_queue:
    if len(q_queue) != len(p_queue):
      return False

    for i in range(len(q_queue)):
      p_node = p_queue.popleft()
      q_node = q_queue.popleft()

      if p_node.val != q_node.val:
        return False

          # Check left children
      if (p_node.left and not q_node.left) or (not p_node.left and q_node.left):
        return False
      if p_node.left and q_node.left:
        p_queue.append(p_node.left)
        q_queue.append(q_node.left)

      # Check right children
      if (p_node.right and not q_node.right) or (not p_node.right and q_node.right):
        return False
      if p_node.right and q_node.right:
        p_queue.append(p_node.right)
        q_queue.append(q_node.right)

  return not p_queue and not q_queue

"""
Optimised solution DFS:
- If there is not a p not and not a q node, return True
- If there is a p node and not q and vice verse, return False
- If values do not match, return False
- Recursively call function or both left and right
"""
def optimised_solution_dfs(p, q):
  if not p and not q:
    return True
  if (p and not q) or (q and not p) or (p.val != q.val):
    return False

  return optimised_solution_dfs(p.left, p.left) and optimised_solution_dfs(p.right, q.right)