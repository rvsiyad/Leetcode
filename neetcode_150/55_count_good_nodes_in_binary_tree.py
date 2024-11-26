"""
Optimal solution:
- We create a global good nodes variable
- Helper function to call recursively, with root and maxNodeVal
- If not root, return 0
- Instantiate the nonlocal variable
- If the roots val is greater or equal to the maxNodeVal
  - Increment global variable and update the maxNodeVal
- Call the function again with the left and right nodes
- Call the recursive function in original function
- Return the good_nodes variable
"""
def optimal_solution(root):
  good_nodes = 0

  def noGreaterNodes(root, maxNodeVal):
    if not root:
      return 0

    nonlocal good_nodes

    if root.val >= maxNodeVal:
      good_nodes += 1
      maxNodeVal = root.val

    noGreaterNodes(root.left, maxNodeVal)
    noGreaterNodes(root.right, maxNodeVal)

  noGreaterNodes(root, root.val)

  return good_nodes