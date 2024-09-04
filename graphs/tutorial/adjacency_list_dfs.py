"""
Imagine we are given a scenario where we need to count the number of paths in an adjacency list, from the source to a destination

We can create a DFS function which takes in a couple parameters:
- The start node
- The target node
- The adjacency list we may have created or been provided with
- visit set() to stop going over the same paths again

We run DFS recursively until on our adjacency list until we reach the target node, after which we will return 1 and increment our count if we find multiple routes.
Once we find our path, we will backtrack and remove nodes from our list and return the count.
"""
def dfs (node, target, adjacencyList, visit): # Create the function with the parameters mentioned
  if node in visit: # If the node is in the visit set, we return 0, since no viable routes this way
    return 0

  if node == target: # If the node is our target, we return 1
    return 1

  count = 0 # Create a count variable, set it to 0
  visit.add(node) # Add the node to the visit set

  for neighbour in adjacencyList[node]: # For each of the neighbours of the node, retrieved using our adjacencyList
    count += dfs(neighbour, target, adjacencyList, visit) # Call the DFS function again, adding the returned value to the count

  visit.remove(node) # We backtrack and remove the node from the visit set

  return count # Return the count

"""
Time complexity:
The number of edges can at most be <= the number of vertices squares -> E <= V^2. This means the DFS solution is exponential.
If we call the avg number of edges N, then we worst case time complexity is O(N^V) : N to the power of V
"""