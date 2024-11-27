"""
Optimal solution:
- Create two sets, one for islands touching pacific and another for atlantic
- Loop through top col and bottom col, passing the indexes to a func to run dfs and add adjacent smaller islands
- Do the same for first and last row
- Now see which over lap, those islands can reach both pacific and atlantic
- Add to res and return res
"""
def optimal_solution(heights):
  ROWS, COLS = len(heights), len(heights[0])
  atlantic = set()
  pacific = set()

  def dfs(row, col, prevHeigh, visited):
    if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited or heights[row][col] < prevHeigh:
      return

    visited.add((row, col))

    dfs(row + 1, col, heights[row][col], visited)
    dfs(row - 1, col, heights[row][col], visited)
    dfs(row, col + 1, heights[row][col], visited)
    dfs(row, col - 1, heights[row][col], visited)

  for col in range(COLS):
    dfs(0, col, heights[0][col], pacific)
    dfs(ROWS - 1, col, heights[ROWS - 1][col], atlantic)

  for row in range(ROWS):
    dfs(row, 0, heights[row][0], pacific)
    dfs(row, COLS - 1, heights[row][COLS - 1], atlantic)

  res = []

  for a in atlantic:
    if a in pacific:
      res.append(a)

  return res
