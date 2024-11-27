"""
Optimal solution:

"""
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

def optimal_solution(root):
  if not root: return None

  oldToNew = {}

  def cloneGraph(node):
    if node in oldToNew:
      return oldToNew[node]

    copy = Node(node.val)
    oldToNew[node] = copy

    for nei in node.neighbors:
      copy.neighbors.append(cloneGraph(nei))

    return copy

  return cloneGraph(root)