"""
Optimal solution:
- Think in reverse, instead of removing surrounded "O", remove "O" not connected to border.
- Create ROW and COL variables
- Loop through border rows and border cols, if we encounter an "O", we run dfs from that point
- The DFS will change all 4-directionally connected "O" nodes into "T".
- Call DFS recursively on neighbours
- Final loop, we check if any rows are left that equal "O", change them to "X" as they are surrounded.
- If we encounter a "T", change back to "O", these are not surrounded.
"""
def optimal_solution(board):
  # Run DFS and chnage all border O to Ts
  ROWS = len(board)
  COLS = len(board[0])

  def dfs(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] == "X" or board[row][col] == "T":
      return

    board[row][col] = "T"
    dfs(row + 1, col)
    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row, col - 1)

  # Do both columns and both rows
  for c in range(COLS):
    if board[0][c] == "O":
      dfs(0, c)

    if board[ROWS - 1][c] == "O":
      dfs(ROWS - 1, c)

  for r in range(ROWS):
    if board[r][0] == "O":
      dfs(r, 0)

    if board[r][COLS - 1] == "O":
      dfs(r, COLS - 1)

  for row in range(ROWS):
    for col in range(COLS):
      if board[row][col] == "O":
        board[row][col] = "X"

      if board[row][col] == "T":
        board[row][col] = "O"
