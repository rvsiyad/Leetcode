import collections

grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

def bfs (grid):
  ROWS, COLUMNS = len(grid), len(grid[0])
  queue = collections.deque()
  visited = set()
  queue.append((0,0))
  visited.add((0,0))

  length = 0

  while queue:
    for i in range(len(queue)):
      r, c = queue.popleft()

      if r == ROWS - 1 and c == COLUMNS - 1:
        return length

      neighbours = [[0,1],[0,-1],[1,0],[-1,0]]

      for dr, dc in neighbours:
        newRow = r + dr
        newColumn = c + dc

        if newRow < 0 or newColumn < 0 or newRow == ROWS or newColumn == COLUMNS or (newRow, newColumn) in visited or grid[newRow][newColumn] == 1:
          continue

        queue.append((newRow, newColumn))
        visited.add((newRow, newColumn))

    length += 1

print(bfs(grid))