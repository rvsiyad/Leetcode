"""
BFS can also be run on a matrix and is most commonly used to find the shortest path in a graph.
BFS matrix is very similar to a tree, but there are a few more edge cases and a different set up - we can move in 4 directions.

Here is an example question:
Q: Find the length of the shortest path from top left of the grid to the bottom right.

Although DFS can also be used to find the shortest path, it is not as efficient.
"""
# Matrix (2D Grid)
import collections

grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

def bfs (grid):
  ROWS, COLUMNS = len(grid), len(grid[0]) # First we initialise our boundaries, for the rows and columns
  visit = set() # We create a hash-set to keep track of visited coordinates
  queue = collections.deque() # Create a queue to keep track of the levels
  queue.append((0,0)) # We append the starting point to both the queue and the visited
  visit.add((0,0))

  length = 0 # Initialise a length variable

  while queue: # While the queue is not empty
    for i in range(len(queue)): # Loop through the length of the queue
      r, c = queue.popleft() # Get the row and column, works like this: [0, 1] by using r,c = [0,1], r = 0, c = 1

      if r == ROWS - 1 and c == COLUMNS - 1: # If any point the row and column are equal to the bottom right end point, we can return the length
        return length

      neighbours = [[0,1], [0,-1], [1, 0], [-1,0]] # We create a neighbours array, holds the different directions we can go - up, down, left, right

      for dr, dc in neighbours: # Loop through the directions
        newRow = r + dr # Add the difference to the current r, and create a newRow variable: This is the neighbours of the popped vertices in the graph matrix
        newColumn = c + dc # Add the different to the current c, create a newColumn variable

        # Edge cases: If the newRow or newColumn is out of bounds or has been visited or is blocked by a 1, then we continue to the next iteration of the loop
        if newRow < 0 or newColumn < 0 or newRow == ROWS or newColumn == COLUMNS or (newRow, newColumn) in visit or grid[newRow][newColumn] == 1:
          continue

        queue.append((newRow, newColumn)) # Else we append the newRow and newColumn coordinates to both the queue and the visited
        visit.add((newRow, newColumn))

    length += 1 # After each loop of the queue, we increment the length

print(bfs(grid))

[[1,0,0],
 [1,1,0],
 [1,1,0]]

[[0,1],
[1,0]]

[[0,0,0],
 [1,1,0],
 [1,1,1]]

[[0,0,0,0,1],
 [1,0,0,0,0],
 [0,1,0,1,0],
 [0,0,0,1,1],
 [0,0,0,1,0]]