"""
Dijkstras is an algorithm within graph problems that can be used to calculate the shortest path in a weighted graph.
It uses a greedy DFS approach alongside a minHeap to carry the minimum cost of the path to each vertices in a graph.

The time complexity of this algorithm is O(E-log-v)

Say we are given a list of edges, which includes the current node, its neighbour and the weight of going from the node to its neighbour.
We can use this to create an adj list and calculate the min weight of travelling between them.
We are also given the number of nodes with the value n and the starting node is src.
"""
import heapq

def shortestPath(edges, n, src):
  adjList = {}

  for i in range(1, n + 1):
    adjList[i] = []

  for s, d, w in edges:
    adjList[s].append([d, w])

  shortest = {}
  minHeap = [[0, src]]

  while minHeap:
    w1, n1 = heapq.heappop(minHeap)

    if n1 in shortest:
      continue

    shortest[n1] = w1

    for n2, w2 in adjList[n1]:
      if n2 not in shortest:
        heapq.heappush(minHeap, [w1 + w2, n2])

  return shortest

