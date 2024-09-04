"""
Difficulty: Medium

Question:
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""
import collections

def shortestPathBinaryMatrix(grid) -> int:
    ROWS, COLUMNS = len(grid), len(grid[0]) # Create variables for the rows and cols of the grid

    if grid[0][0] == 1 or grid[ROWS -1][COLUMNS -1] == 1: # If the start or ends are blocked by 0, return -1 since a route is impossible
      return -1

    queue = collections.deque() # Create our queue and append the start index
    queue.append((0,0))

    grid[0][0] = 1 # Also change it to 1, so that it is shown as visited

    length = 1 # Our current length is 1

    while queue: # While the queue is not empty
      for i in range(len(queue)): # Loop through the current length of the queue
        r, c = queue.popleft() # Get the row and cols of the left most value in the queue

        if r == ROWS -1 and c == COLUMNS -1: # If the indexes are at the end of the matrix, return the length
          return length

        directions = [[0,1],[0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1, 1], [-1,-1]] # Create the directions array

        for dr, dc in directions: # For each coordinate
          newRow = r + dr # Create the newRow and newCol
          newColumn = c + dc

          # If out of bounds or grid[index][index] is 1 so is blocked, continue to the next iteration of the loop
          if newRow < 0 or newColumn < 0 or newRow == ROWS or newColumn == COLUMNS or grid[newRow][newColumn] == 1:
            continue

          grid[newRow][newColumn] = 1 # If not, make it a 1
          queue.append((newRow, newColumn)) # Append the newRow and newCol to the queue

      length += 1 # Each while loop, increment the length by 1
    return -1 # If the end cannot be reached, return -1