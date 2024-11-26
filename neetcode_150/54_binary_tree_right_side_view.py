"""
Optimal solution:
- If not root, return an empty array
- Create results array
- Create a queue and append the root
- While queue
- Create a last index variable which holds len(queue) - 1
- Loop through the length of queue
- Popleft from the queue
- If i index == lastIndex, append node val to res
- Append children of node to queue, left first then right
- Return the result arr
"""
from collections import deque

def optimal_solution(root):
  if not root:
    return []
  # BFS last node in each level
  result = []
  queue = deque()

  queue.append(root)

  # If i == last index, append to result
  while queue:
    lastIndex = len(queue) - 1

    for i in range(len(queue)):
      node = queue.popleft()

      if i == lastIndex:
        result.append(node.val)

      if node.left:
        queue.append(node.left)

      if node.right:
        queue.append(node.right)

  return result