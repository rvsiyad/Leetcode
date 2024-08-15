"""
Difficulty: Medium

Question:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighbouring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
"""
def exist(board, word):
  ROWS = len(board) # Get the number of rows in the matrix
  COLUMNS = len(board[0]) # Get the number of columns in the matrix
  path = set() # Create a path set to keep track of the path of rows/columns we have traversed

  def backtrack(r, c, i): # Create a backtrack function which takes in the row column and the index of the word
    if i > len(word) - 1: # If the pointer i, is greater than the last index of the word, return true
      return True

    # Here are a number of edge cases that can make the word search invalid,
    # If the row or columns are out of bounds, so over the length or below 0, or if the word does not match the board or if the path has been traversed before
    if r >= ROWS or c >= COLUMNS or r < 0 or c < 0 or word[i] != board[r][c] or (r,c) in path:
      return False # Then we can return false

    path.add((r,c)) # We add our location in the matrix to the set
    res = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1) # Recursively call backtrack to all locations above, below and to left and right
    path.remove((r, c)) # Then we backtrack and remove the path,

    return res # Then we return the result, to see if any return True

  # Now we make our recursive call to each and every index in the matrix
  for R in range(ROWS): # Loop through each row
    for C in range(COLUMNS): # Loop through each column
      if backtrack(R, C, 0): # Call our recursive function with the R and C indexes and the word index of 0
        return True # If the backtrack() returns true, we return true
  return False # Else we return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
"""
Notes
"""