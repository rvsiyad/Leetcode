"""
Optimal solution:
- Create an adjacency graph for the courses and prerequisites
- Do this by looping from 0 to number of courses, as empty prereqs means that course can be taken
- Create a set to keep track of courses taken
- Do DFS on each course, if we can do it, return True
- Add each course to the set, if we see a course in the set already, there is a loop, return False
- Loop through all courses, see if possible to do all courses, return False if not.
"""
def optimal_solution(numCourses, prerequisites):
  courseToPre = {}

  for i in range(numCourses):
    courseToPre[i] = []

  visited = set()

  for crs, pre in prerequisites:
    if crs not in courseToPre:
      courseToPre[crs] = [pre]
    else:
      courseToPre[crs].append(pre)

  def dfs(crs):
    if crs in visited or crs not in courseToPre:
      return False

    if courseToPre[crs] == []:
      return True

    visited.add(crs)

    for pre in courseToPre[crs]:
      if not dfs(pre):
        return False

    visited.remove(crs)
    return True


  for i in range(numCourses):
    if not dfs(i):
      return False

  return True