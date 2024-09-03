"""
DFS as previously mentioned is a very popular technique and as such can be used with graphs in matrix form.
Being able to conduct DFS on a matrix can be useful as we can search all possible "routes" within a matrix and
based on that conduct some logic, for example counting the number of valid paths from A to B.

DFS allows us to traverse a matrix similar to how we would traverse a tree. In a matrix we can move in 4
different directions - left, right, up, and down.

Take the following question for example:
Q: Count the unique paths from the top left to the bottom right. A single path may only move along 0's and can't visit the same cell more than once.

matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

When considering this type of question, we need to consider the base cases. One case where we do not have a valid path, and another where we do have a valid path.
From this we can then work through using backtracking, to retrace our steps and attempt another route.
"""
def countUniquePaths(matrix):
  def dfs(matrix, r,c, visited):
    if(r < 0 or c < 0 or r == len(matrix) or c == len(matrix[0]) or matrix[r][c] == 1 or (r,c) in visited):
      return 0
    if (r == len(matrix) - 1 and c == len(matrix[0]) - 1):
      return 1

    visited.add((r,c))

    count = 0

    count += dfs(matrix, r + 1, c, visited)
    count += dfs(matrix, r - 1, c, visited)
    count += dfs(matrix, r, c + 1, visited)
    count += dfs(matrix, r, c - 1, visited)

    visited.remove((r,c))

    return count

  return dfs(matrix, 0, 0, set())

matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

print(countUniquePaths(matrix))