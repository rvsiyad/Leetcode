"""
Optimised iterative approach:
- Create prev and curr pointers
- While curr
- Create tmp variable for curr.next
- Set curr.next to prev
- Set prev to curr
- Set curr to tmp variable
- Return prev
"""
def optimised_solution(head):
  prev, curr = None, head

  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

  return prev
