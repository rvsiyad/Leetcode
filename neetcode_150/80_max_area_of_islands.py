"""
Optimal solution:
- Similar to most graph problems
- Loop through grid
- DFS for each islands
- If out of bounds return 0
- Change grid to 0 if 1
- Accumulate area by adding to current area value of 1
- Outside func call, compare against current max
"""
def optimal_solution(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  def calculateArea(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0:
      return 0

    grid[row][col] = 0
    area = 1 + calculateArea(row + 1, col) + calculateArea(row - 1, col) + calculateArea(row, col + 1) + calculateArea(row, col - 1)
    return area

  area_islands = 0

  for row in range(ROWS):
    for col in range(COLS):
      area_islands = max(area_islands, calculateArea(row, col))

  return area_islands