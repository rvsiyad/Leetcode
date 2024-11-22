"""
Brute force solution:
- Rows:
  - Loop through each row horizontally.
  - Create a set to keep track of seen nums
  - Loop through each value in the row horizontally.
  - If we encounter a "." we continue
  - If the value is in seen, we can return false
  - Else add value to the seen set.

- Columns:
  - Loop through each column vertically.
  - Create a set to keep track of seen nums
  - Loop through each value in the column vertically.
  - If we encounter a "." we continue
  - If the value is in seen, we can return false
  - Else add value to the seen set.

- Squares:
  - Loop through each of the 9 possible squares
  - Create a set to keep track of seen nums.
  - For each 3x3 row col in the square
  - The correct squares row is calculated by:
    - (Floor division of the current square ) * 3 + index for row
  - The correct squares col is calculated by:
    - (Square modulo 3) * 3 + index for col
  - If we encounter a "." we continue
  - If the value is in seen, we can return false
  - Else add value to the seen set.

  - Return true if all else.
"""
def brute_force_solution(board):
  for row in range(9):
    seen = set()
    for i in range(9):
      if board[row][i] == ".":
        continue

      if board[row][i] in seen:
        return False

      seen.add(board[row][i])

  for col in range(9):
    seen = set()
    for i in range(9):
      if board[i][col] == ".":
        continue
      if board[i][col] in seen:
        return False
      seen.add(board[i][col])

  for square in range(9):
    seen = set()

    for i in range(3):
      for j in range(3):
        row = (square//3) * 3 + i
        col = (square%3) * 3 + j

        if board[row][col] == ".":
          continue

        if board[row][col] in seen:
          return False

        seen.add(board[row][col])

  return True


"""
Optimal solution:
- Create hashmaps with sets as the values
  - One hashmap for rows
  - One for columns
  - One for the squares
- Loop through each row and column in the board
- If current board val is a "." we continue
- If board val appears in the row and col, return false
- Square is more complex by is done by just creating dedicated squares, the key is the starting index of that square
- Add values to the dedicated hashmaps
- Return true if no false's are returned.
"""
from collections import defaultdict

def optimal_solution(board):
  rowSet = defaultdict(set)
  colSet = defaultdict(set)
  squareSet = defaultdict(set)

  for row in range(9):
    for col in range(9):
      if board[row][col] == ".":
        continue

      if( board[row][col] in rowSet[row] or board[row][col] in colSet[col] or board[row][col] in squareSet[(row // 3, col // 3)]):
        return False

      rowSet[row].add(board[row][col])
      colSet[col].add(board[row][col])
      squareSet[(row // 3, col // 3)].add(board[row][col])

  return True