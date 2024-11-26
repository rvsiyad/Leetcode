"""
Optimal solution:
- If not root, return empty arr
- Create a queue and append root to it
- While queue is populated
- Create empty level array
- Loop through length of the queue
- popleft from queue and add value to level array
- If it has left or right children, add to queue
- Outside for loop, add level arr to res array
- Return res array
"""
from collections import deque

def optimal_solution(root):
  if not root:
    return []

  res = []
  queue = deque()

  queue.append(root)

  while queue:
    level_order_arr = []

    for i in range(len(queue)):
      node = queue.popleft()

      level_order_arr.append(node.val)

      if node.left:
        queue.append(node.left)

      if node.right:
        queue.append(node.right)

    res.append(level_order_arr)

  return res