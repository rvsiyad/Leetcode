"""
Optimal solution:
- To complete this problem efficiently, we can use a variation of BFS
- Add all chests and go backwards from here to assign empty squares a distance from the chest
- Create a queue, visited set to not revisit cells, and ROWS and COLS.
- Loop through all rows and cols and add the row, col pairs where it is a chest to the queue and set
- After this, create a distance variable
- While queue, loop through length of the queue
- Pop from the queue
- If the grid value at row, col != 0 and != -1, update to distance
- Create helper function to add the (row, col) pair in all 4 directions to the queue and visited
- Outside for loop, increment distance
"""
from collections import deque

def optimal_solution(grid):
  ROWS, COLS = len(grid), len(grid[0])
  queue = deque()
  visited = set()

  def addLand(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or grid[row][col] == -1:
      return
    else:
      queue.append((row, col))
      visited.add((row, col))

  for row in range(ROWS):
    for col in range(COLS):
      if grid[row][col] == 0:
        queue.append((row, col))
        visited.add((row, col))

  distance = 0

  while queue:
    for i in range(len(queue)):
      row, col = queue.popleft()

      if grid[row][col] != 0 and grid[row][col] != -1:
        grid[row][col] = distance

      addLand(row + 1, col)
      addLand(row - 1, col)
      addLand(row, col + 1)
      addLand(row, col - 1)

    distance += 1