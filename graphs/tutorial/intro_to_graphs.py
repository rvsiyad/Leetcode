"""
Graphs are made of nodes - similar to trees - where the nodes may be connected by pointers.
  - Nodes are referred to as `vertices` within a graph and the pointers connecting vertices are called `edges`
  - It is possible to have graphs with no edges, but the maximum amount of edges is <= to the number of vertices squared - E = V^2.
  - Vertices can point to itself and other nodes.
  - Directed graphs: Where the pointers connecting the edges have a direction.
  - Undirected graphs: Where the pointers connecting the edges have no direction.
"""
grid = [[0, 0, 0, 0], # The grid is a 4*4 array which can be indexed like so:
        [1, 1, 0, 0], # grid[0][0] - This gives us the first row, and the first value in the column
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
""""
Graph questions are normally represented in 3 different ways as it is an abstract concept which can be implemented via different data structures.
  - Matrix:
    - A two dimensional array with rows and columns, which can represent a graph.
    - The first level represents the rows and within the second level, we find the columns.
    - The time and space complexity to traverse the grid is 0(n * m).
    - How this can represent a graph?:
      - In the example below, the 0's represent the vertices, from which we can move up, down, left and right.
      - Adjacent 0's are connected via edges, and 1's are blocked.
"""

adjMatrix = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
"""
  - Adjacency Matrix:
    - This is a less common input format where the indexes themselves represent the vertices.
    - 0 represents there is no edges between vertices while 1 denotes there is an edge.
    - The connection of edges is represented by the indexes, [v1, v2], where v1 is the row and v2 is the column.
    - adjMatrix[1][2] == 0 meaning there is no edge from vertices 1 to vertices 2.
    - adjMatrix[2][1] == 1 meaning there is an edge from vertices 2 to vertices 1.
"""

class GraphNode:
  def __init__(self, val):
    self.val = val
    self.neighbours = []
"""
  - Adjacency List:
    - Uses a class to store the nodes values and a list of pointers to other vertices with edges connected.
    - This is much more efficient than an adjacency matrix as it only stores edges that exist.
"""