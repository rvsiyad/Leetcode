"""
Optimal solution:
- Similar to course schedule one except we need to keep track of an order we can complete all courses
- This is a form of topological sort
- Create an array to hold the order of the courses
- Create two sets, one for visited detections and another to check if in res
- We create the adj list for the course and prereq courses
- We loop over the courses and make sure we can dfs the courses, if we cannot, return an empty array
- We create the DFS function, this takes in the course
- If the course is in the visited set, we have a loop, we return False
- If the course has no prereqs, we can return true, but let's also add to our res by first checking it is not inside the res set
- We add the course to the visit set
- Loop through the courses prereqs and conduct DFS on that also, return False if dfs returns False
- Backtrack and remove course from the set()
- Before the return True statement, add the course to both the res array and the inRes set, if not already in res set.
"""
def optimal_solution(numCourses, prerequisites):
  res = []

  courseToPre = {}

  for i in range(numCourses):
    courseToPre[i] = []

  for crs, pre in prerequisites:
    courseToPre[crs].append(pre)

  visited, inRes = set(), set()

  def dfs(crs):
    if crs not in courseToPre or crs in visited:
      return False

    if courseToPre[crs] == []:
      if crs not in inRes:
        res.append(crs)
        inRes.add(crs)

      return True

    visited.add(crs)

    for pre in courseToPre[crs]:
      if not dfs(pre):
        return False

    visited.remove(crs)

    if crs not in inRes:
      res.append(crs)
      inRes.add(crs)

    return True


  for i in range(numCourses):
    if not dfs(i):
      return []

  return res
