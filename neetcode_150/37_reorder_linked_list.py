"""
Optimised solution:
- To merge the two lists, we need to split the list in two
- Then reverse the second list and merge in order of list1 ad then list2
- Merge as list1, list2, list1, list2
- Merge if any remainders of lists are present.
"""
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def optimised_solution(head):
  # Split into two lists, by finding midpoint and splitting
  slowPointer = head
  fastPointer = head

  while fastPointer and fastPointer.next:
    slowPointer = slowPointer.next
    fastPointer = fastPointer.next.next

  # Slow pointer now at midpoint
  secondList = slowPointer.next
  slowPointer.next = None

  # Reverse the second list
  curr = secondList
  prev = None

  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

  list1 = head
  list2 = prev

  dummyNode = ListNode()

  curr = dummyNode

  while list1 and list2:
    curr.next = list1
    list1 = list1.next

    curr = curr.next

    if list2:
      curr.next = list2
      list2 = list2.next
      curr = curr.next

  if list1:
    curr.next = list1

  if list2:
    curr.next = list2