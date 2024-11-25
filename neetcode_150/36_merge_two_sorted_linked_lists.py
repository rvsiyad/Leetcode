"""
Optimal solution:
- Create a dummyNode
- Assign curr to the dummy node
- While list1 and list2
- Assigned the smallest of the list node vals to curr.next
- update list nodes to list node .next
- Check if any of the lists remain, merge as curr.next
- Return the dummyNode.next as the head
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def optimal_solution(list1, list2):
  dummy = node = ListNode()

  while list1 and list2:
    if list1.val < list2.val:
      node.next = list1
      list1 = list1.next
    else:
      node.next = list2
      list2 = list2.next
    node = node.next

  node.next = list1 or list2

  return dummy.next