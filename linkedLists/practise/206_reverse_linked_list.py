class ReverseLinkedList:
  """
  Difficulty: Easy

  Question:
  Given the head of a singly linked list, reverse the list, and return the reversed list.

  Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]

  Example 2:
  Input: head = [1,2]
  Output: [2,1]

  Example 3:
  Input: head = []
  Output: []
  """

  def reverseLinkedList(head):
    prev, curr = None, head # First we create two pointers, one to the previous

    while curr is not None: # While curr is not null, loop through the linked list
      nxt = curr.next # We store the next nodes location in the variable nxt

      curr.next = prev # We set next nodes location to that of the previous pointer
      prev = curr # Set the prev pointer to point at the curr node
      curr = nxt # We set the curr pointer to point at the next node.

    return prev # We can return previous as it is pointing at the new head.


  """
    Example:
    None  [1] -> [2] -> [3] -> [4] -> [5] - None
    p      c

    Iteration 1:
    prev = None
    curr = [1]

    while curr is not None:
      nxt = curr.next == [2]  // Save the next nodes location for later.
      curr.next = prev == None // Here [1] was pointing to [2], [1] is now pointing to None.
      prev = [1] // Move the pointer up to the curr location.
      curr = [2] // Move the curr pointer up a node, using the nxt variable from earlier.

    Current Linked List standing:
    None <- [1]  [2] -> [3] -> [4] -> [5] - None
            p    c

    Iteration 2:
    prev = [1]
    curr = [2]

    while curr it not None:
    nxt = curr.next == [3]
    curr.next = prev == [1]
    prev = curr = [2]
    curr = nxt == [3]

    Current Linked List standing:
    None <- [1] <- [2] [3] -> [4] -> [5] - None
                    p    c
  """
