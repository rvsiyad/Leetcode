class DummyNodes:
  """
  Dummy nodes are a technique that are normally used with Linked Lists questions. They allow us to create a new "dummy" node from which can join to
  other nodes which meet the requirements needed within a specific scenario.

  For example, if we have a list of numbers greater and smaller than x, we can set up two dummy nodes, one called "greater" and another "smaller", from
  which we can append nodes which meet the requirements. The two nodes can later be joined via the dummy heads but calling greater.next and smaller.next.
  """
  def partition(self, head: ListNode, x: int) -> ListNode:                                                                            # type: ignore
        # Create two dummy nodes to start the less and greater lists
        less_dummy = ListNode(0)                                                                                                      # type: ignore
        greater_dummy = ListNode(0)                                                                                                   # type: ignore

        # Pointers for the current node in less and greater lists
        less = less_dummy
        greater = greater_dummy

        # Traverse the original list and partition the nodes
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        # Combine the two lists
        greater.next = None  # End the greater list
        less.next = greater_dummy.next  # Link the end of less list to the beginning of greater list

        # Return the start of the less list
        return less_dummy.next