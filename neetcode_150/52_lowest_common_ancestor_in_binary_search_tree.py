"""
Optimal solution:
- Create helper function to call recursively
- If the root.val is equal to val of p or q, return True
- If the max value of p.val and q.val is smaller than the root.val, recursively return check left child
- If the min value of p.val and q.val is greater than the root.val, recursively return check right child
- Call recursive func and return node
"""
def optimal_solution(root, p, q):
  def lca(root, p, q):
    if root.val == p.val or root.val == q.val:
      return root

    if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
      return root

    if max(p.val, q.val) < root.val:
      return lca(root.left, p, q)
    elif max(p.val, q.val) > root.val:
      return lca(root.right, p, q)

  return lca(root, p, q)