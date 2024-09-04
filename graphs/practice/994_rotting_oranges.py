"""
Difficulty: Medium

Question:
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
import collections

def rottingOranges(grid):
  queue = collections.deque() # Create the queue which will hold the rotten oranges
  timeTaken, freshOranges = 0, 0 # Create variables to keep track of the timeTaken and the number of freshOranges

  ROWS, COLS = len(grid), len(grid[0]) # Get the number of ROWS and COLS in the grid

  for r in range(ROWS): # Loop through the grid
    for c in range(COLS):
      if grid[r][c] == 1: # If we find a fresh orange, increase the count
        freshOranges += 1

      if grid[r][c] == 2: # If we find a rotten orange, add it to the queue
        queue.append((r,c))

  while queue and freshOranges > 0: # While the queue is not empty and the number of freshOranges is greater than 0
    for i in range(len(queue)): # Loop through the current number of values in the queue
      r, c = queue.popleft() # Pop from the left of the queue and assign the rows and cols
      directions = [[1, 0], [-1, 0], [0,1], [0, -1]] # Create our directions

      for dr, dc in directions: # Loop through the directions
        newRow, newCol = dr + r, dc + c # Create the newRow and newCol which holds the up, down, left and right coordinates

        # If out of bounds or any of the grids are not a 1, then we can continue to the next loop
        if newRow < 0 or newCol < 0 or newRow == ROWS or newCol == COLS or grid[newRow][newCol] != 1:
          continue

        grid[newRow][newCol] = 2 # Else make the adjacents rotten
        queue.append((newRow, newCol)) # And append them to the queue
        freshOranges -= 1 # Decrement the number of fresh oranges

    timeTaken += 1 # Increase the time take after each while loop

  return timeTaken if freshOranges == 0 else -1 # Return the timeTaken only if the number of freshOranges is 0

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rottingOranges(grid))
"""
Notes:
This is a tricky question if the trick is not shown. As there can be many rottenOranges in different locations, we should first loop over
the entire grid, adding the index to the queue. After we fill the queue, then we work from there.
"""