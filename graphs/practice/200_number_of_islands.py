"""
Difficulty: Medium

Question:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
def numberOfIslands(grid):
  def dfs(r, c): # We create a helper function which takes in the coordinates in the grid
    ROWS, COLUMNS = len(grid) - 1, len(grid[0]) - 1 # Get the indexes for the grids ROWS and COLUMNS

    # These are the edge cases which terminate the dfs, if r or c is out of bounds or if the coordinates point to a 0.
    if r < 0 or c < 0 or r > ROWS or c > COLUMNS or grid[r][c] == "0":
      return # Then we return
    else:
      grid[r][c] = "0" # Else it is a 1, we turn it into a zero, so it is not counted as an island again.

      dfs(r + 1, c) # Then we DFS for the positions, above, below, to the right, and left.
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)

  numIslands = 0 # Outside our helper function, we create a variable to hold our result

  for i in range(len(grid)): # We loop through the grid using a double for loop
    for j in range(len(grid[0])):
      if grid[i][j] == "1": # If the index values equal a 1, we found an island.
        numIslands += 1 # Increment the count by 1
        dfs(i,j) # Run the dfs helper function from those indexes

  return numIslands # Return the number of islands.