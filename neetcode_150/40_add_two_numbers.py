"""
Optimised approach with O(n) space:
- Populated 2 strings with values of the linked lists
- Reverse the two strings
- Add the values together using int conversion
- Create a new list using the values in the string combined values
- Make sure to int conversion, and iterate over the loop backwards.
- Return new head.
"""
class ListNode():
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def optimised_approach_no1(l1, l2):
  # 1 -> 2 -> 3
  # 4 -> 5 -> 6
  l1String, l2String = "", ""

  l1Pointer, l2Pointer = l1, l2

  while l1Pointer:
    l1String += str(l1Pointer.val)
    l1Pointer = l1Pointer.next

  while l2Pointer:
    l2String += str(l2Pointer.val)
    l2Pointer = l2Pointer.next

  l1String = l1String[::-1]
  l2String = l2String[::-1]

  newTotal = int(l1String) + int(l2String)
  newTotal = str(newTotal)

  dummyNode = ListNode()
  curr = dummyNode

  for i in range(len(newTotal) -1, -1, -1):
    curr.next = ListNode(newTotal[i])
    curr = curr.next

  return dummyNode.next


"""
Optimised approach
"""