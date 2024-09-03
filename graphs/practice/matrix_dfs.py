# You are given a grid, now traverse it and the number of routes.
gridMatrix = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

def traverseMatrix(r,c,matrix,visited):
  ROWS = len(matrix) - 1
  COLUMNS = len(matrix[0]) - 1

  if (r < 0 or c < 0 or r > ROWS or c > COLUMNS or matrix[r][c] == 1 or (r,c) in visited):
    return 0

  if (r == ROWS and c == COLUMNS):
    return 1

  visited.add((r,c))

  count = 0
  count += traverseMatrix(r + 1, c, matrix, visited)
  count += traverseMatrix(r - 1, c, matrix, visited)
  count += traverseMatrix(r, c + 1, matrix, visited)
  count += traverseMatrix(r, c - 1, matrix, visited)

  visited.remove((r,c))

  return count

print(traverseMatrix(0, 0, gridMatrix, set()))