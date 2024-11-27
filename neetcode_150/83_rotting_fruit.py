"""
Optimal solution:
- Multi-BFS approach
- Count fresh fruit and add rotten to queue
- Go through queue and while there are fresh fruit
- Add adjacent bananas to queue if not rotten.
- Increment at each while loop
- Return mins taken if fresh == 0, else -1
"""
from collections import deque

def optimal_solution(grid):
  ROWS, COLS = len(grid), len(grid[0])
  queue = deque()
  fresh = 0

  for row in range(ROWS):
    for col in range(COLS):
      if grid[row][col] == 2:
        queue.append((row, col))

      if grid[row][col] == 1:
        fresh += 1

  mins_taken = 0

  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  while queue and fresh > 0:
    for i in range(len(queue)):
      row, col = queue.popleft()

      for dr, dc in directions:
        r, c = row + dr, col + dc

        if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
          grid[r][c] = 2
          fresh -= 1
          queue.append((r, c))

    mins_taken += 1

  return mins_taken if fresh == 0 else -1