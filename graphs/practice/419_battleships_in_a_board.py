"""
Difficulty: Medium

Question:
Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board.
In other words, they can only be made of the shape 1 x k (1 row, k columns)
or k x 1 (k rows, 1 column), where k can be of any size.
At least one horizontal or vertical cell separates between two battleships
(i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0
"""

def countBattleships(board):
  # Get the ROWS and COLUMNS indexes
  ROWS = len(board) - 1
  COLUMNS = len(board[0]) - 1

  battleShips = 0 # Create a variable which will hold the number of battle ships

  for row in range(len(board)): # Loop through the matrix
    for column in range(len(board[0])):
      if board[row][column] == "X": # If we encounter a battle ship
        if (row + 1) <= ROWS and board[row + 1][column] == "X": # If the battleship is vertical
          currRow = row # Create a currRow which holds the row
          while (currRow) <= ROWS and board[currRow][column] == "X": # While currRow is in-bounds and the grid coordinates is "X"
            board[currRow][column] = '.' # Remove the battle ship
            currRow += 1 # Increment the currRow by 1
        elif (column + 1) <= COLUMNS and board[row][column + 1] == "X": # If the battleship is horizontal
          currColumn = column # Create a currColumn variable which holds the column
          while (currColumn) <= COLUMNS and board[row][currColumn] == "X": # While currColumn is in-bounds and the grid coordinates is "X"
            board[row][currColumn] = '.' # Remove the battleShip
            currColumn += 1 # Increment the currColumn by 1
        else:
          board[row][column] = '.' # Else it is a battleShip of size 1, remove it.

        battleShips += 1 # Increment the battleship count by 1

  return battleShips # Return the number of battleships

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

countBattleships(board)