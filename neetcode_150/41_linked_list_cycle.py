"""
Optimal solution:
- Create a fastPointer and slowPointer, both at head
- While fastP in bounds and there is fastP.next
- Increment slowP to next and fastP to next next
- If they are equal, return True
- Return False
"""
def optimal_solution(head):
  slowP = head
  fastP = head

  while fastP and fastP.next:
    slowP = slowP.next
    fastP = fastP.next.next

    if slowP == fastP:
      return True

  return False