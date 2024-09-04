"""
Imagine we are in a scenario where we want to find the shortest path from our source node to a target destination. The best way to do this
is via BFS on an adjacency list. The solution is very similar to the matrix BFS but we no longer have to worry about edge cases, like out of bounds.

Our BFS solution will take 3 parameters for this solution:
  - The source node
  - The target node
  - The adjacency list, which we may have created or been provided with
"""
import collections

def bfs (node, target, adjacencyList): # We pass the node, the target node, and the adjacency list
  length = 0 # Create a length variable

  visit = set() # Create a visit set and add the current node
  visit.add(node)

  queue = collections.deque() # Create a queue and add the current node
  queue.append(node)

  while queue: # While the queue is not empty
    for i in range(len(queue)): # Loop through the current length of the queue
      curr = queue.popleft() # The left most node in the queue is popped and assigned as the current node

      if curr == target: # If the current node is the target, return the length of the shortest path
        return length

      for neighbour in adjacencyList[curr]: # Else we continue by looping through all of the current nodes neighbours in the adjacency list
        if neighbour not in visit: # If the neighbour has not been visited, hence not in the visit set,
          queue.append(neighbour) # Append and add the neighbour to the queue and visit set respectively
          visit.add(neighbour)
    length += 1 # Each iteration of the while loop, increment the length by 1

  return length # After the while loop completes, return the length

"""
Time complexity:
With BFS solution, we know we do not have a exponential time complexity as we do not have self loops and we don't have the max number of edges.
Therefore in the worst possible case our BFS solution will visit every node and traverse every edge, making the time complexity O(V + E),
where V is the number of vertices and E is the number of edges.
"""