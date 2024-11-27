"""
Optimal solution:
- Create numOfIslands variable
- Gets num of ROwWS and COLS
- Create a helper function that will remove islands
  - If out of bounds or not island, return
  - Change 1's to 0
  - Recursively call functions in all 4 directions
- Loop through rows and cols
- If index is a "1", call the helper func on that index
- Increment num_islands count
- Return it
"""
def optimal_solution(grid):
  num_islands = 0
  ROWS = len(grid)
  COLS = len(grid[0])

  def remove_island(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
      return

    if grid[row][col] == "1":
      grid[row][col] = "0"

    remove_island(row + 1, col)
    remove_island(row - 1, col)
    remove_island(row, col + 1)
    remove_island(row, col - 1)

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == "1":
        num_islands += 1
        remove_island(row, col)

  return num_islands