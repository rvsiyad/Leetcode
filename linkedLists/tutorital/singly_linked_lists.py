class SinglyLinkedList:
  """
  - Introduction:
    Linked lists are like an array but some differences.

    First linked lists are made up of listNodes. Each node can contain two values: a Value, and Next.

    The value can be anything from a int, string, character etc...
    The next stores a references to the next node in the linkedList.

    Linked lists are not stored in a contiguous location in memory, and remain in a random area in memory.
    They are linked via the next, which points to the next nodes location in memory.

    Normally, at least one of the following values are provided in a LeetCode question:
      - The head: This is the first node of the Linked List
      - The tail: This is the last node of the Linked List

      By having the start or end nodes we can traverse the linked list.
  """

  # - Creating a Linked List from scratch:
  def __init__(self, val):
    self.val = val # Here we are setting the current nodes value.
    self.next = None # The next value holds the location of the next node in the linked list.

  # - Setting the next node in the Linked List:
    ListNode1.next = ListNode2  # type: ignore
    ListNode2.next = ListNode3  # type: ignore
    ListNode3 = None

  # Traversing over a Linked List:
  cur = ListNode1  # type: ignore

  while cur: # This is able to traverse over the linked list as long as cur is not null.
    cur = cur.next # When the cur.next is None, such as for ListNode3, the Loop will end.

  # Circular Linked List are different from a normal linked list in the fact that the last node,
  # points to the first not. So in our previous example, ListNode3 would point back to ListNode1

  ListNode3.next = ListNode1  # type: ignore


  # Operations that can be performed on a LinkedList:
  # - Appending a new node:
  #   This is a simple operation where the new node is set as the next node, after the tail.
  #   And the tail is then updated to be the next node.

  tail.next = ListNode4  # type: ignore
  tail = ListNode4  # type: ignore

  # - Deleting a node:
  #   Removing a node from a LinkedList is fairly simple. It requires us to set the next pointer for the previous
  #   node before y to the point at the node after y. The removed node does not have to be deleted as it is in memory,
  #   and will be removed via pythons built in garbage collector.

  head.next = head.next.next  # type: ignore

  # This skips over the 2nd node in the Linked List, connecting ListNode1 to ListNode3.

