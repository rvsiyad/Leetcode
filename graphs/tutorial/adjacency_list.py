"""
Adjacency lists provide an easier way to traverse a graph than matrices. They allow us to easily find the neighbours of a vertex and no
longer have to worry about going out of bounds, removing a lot of boiler plate code.

For questions on adjacency lists, we can mostly expected to build the adjacency list ourselves. We are provided with a list of directed edges
and have to build an adjacency list from it.

The code below shows how to code this:
"""
# Given directed edges, build an adjacency list. The Lists inside represent the vertices and its edge ->  [Node, edgeTo]
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

def buildAdjacencyList(edges): # If we are passed these edges in a question, we can create an adjList
  adjList = {} # We use a dictionary to hold the vertices as the key and the edges to other nodes as values

  for src, dst in edges: # For each src "source" and each dst "destination" in the edges
    if src not in adjList: # If src not in adjList, we add to the adjList hashmap
      adjList[src] = []
    if dst not in adjList: # If dst not in adjList, we add to the adjList hashmap
      adjList[dst] = []

    adjList[src].append(dst) # Once both are added to the hashmap or already present, we add the new destination value to the src key in the hashmap

  return adjList # We can return the adjList

adjList = buildAdjacencyList(edges)
print(adjList) # -> {'A': ['B'], 'B': ['C', 'E'], 'C': ['E'], 'E': ['D'], 'D': []}