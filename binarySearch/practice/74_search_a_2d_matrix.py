def searchMatrix(matrix, target):
  # First we need to run a binary search to figure out what row we need to be on
  # To do this, we can run a binary search to find the middle row, and from there check if the
  # value at the current rows column is greater or smaller than the first and last values.
  rows, columns = len(matrix), len(matrix[0]) # The rows is the number of arrays in the matrix, and the columns in the number of values in the array
  top, bottom = 0, rows - 1 # Create our two high and lows (our pointers for the correct row).

  while top <= bottom: # Loop through while the top is smaller or equal to the bottom
    row = (top + bottom) // 2 # Take our middle row

    if target > matrix[row][-1]: # If the target is greater than the largest value in the current row, move the top pointer to the middle + 1
      top = row + 1
    elif target < matrix[row][0]: # If the target is smaller than the smallest value in the current row, move the bottom pointer to the middle - 1.
      bottom = row - 1
    else:
      break # If the target is equal or between those ranges, we break the loop.

  if top > bottom: # Check if the loop exceeded by checking if the top is now greater than the bottom.
    return False

  L, R = 0, columns - 1 # Take the Left and Right pointers, set via the length of the columns

  while L <= R: # While the Left pointer is smaller/equal to the right pointer
    m = (L + R) // 2 # Calculate the middle between the L and R

    if target > matrix[row][m]: # If the target is greater than the current rows middle, move the L pointer to the middle + 1
      L = m + 1
    elif target < matrix[row][m]: # If the target is smaller than the current rows middle, move the R pointer to the middle - 1
      R = m - 1
    else:
      return True # If it is equal, then we return True

  return False # If all checks fail, we return False.