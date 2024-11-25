"""
Optimal solution:
- We use a two pointer approach to remove nodes
- We create a dummyNode, both to use as the L pointer starting point and what to return (dummy.next)
- We keep moving the R pointer up the list until n is reached
- We now increment the right and left pointers while R is not null
- Once this while loop ends, we can use the L pointer to make the nodes next value that of the next nodes next.
- Return the dummyNode.next
"""
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def optimal_solution(head):
  dummyNode = ListNode(0, head)

  left = dummyNode
  right = head

  while n > 0 and right:
    n -= 1
    right = right.next

  while right:
    right = right.next
    left = left.next

  left.next = left.next.next

  return dummyNode.next