class DoublyLinkedLists:
  """
  - Introduction:
    Doubly Linked Lists are similar to a singly Linked List with one added variation. As the name
    suggests, they include an extra pointer called prev which points to the previous Node. This
    allows us to traverse forwards or backwards over the Linked List.

  """
  # - Creating a doubly linked list from scratch:
  def __init__(self, val):
    self.val = val # Here we are setting the current nodes value.
    self.next = None # The next value holds the location of the next node in the linked list.
    self.prev = None # The previous value holds the location of the previous node in the linked list.

  # - Inserting at the end of a doubly linked list:
  def insert(tail, ListNode4):
    tail.next = ListNode4 # The end of the tail now connects to the new node.
    ListNode4.prev = tail # We can set the previous value for the new node as the current tail.
    tail = tail.next # Update the tail to be the new node added.

    return tail # Return the new tail

  # - Deleting from a doubly linked list:
  def delete(tail):
    ListNode2 = tail.prev # We assign the tails previous value to a variable
    ListNode2.next = None # Set the nodes next variable to None, cutting off the link.
    tail = ListNode2 # Assign the tail to the previous node.

    return tail # Return the new tail

  """
  Closing notes:
    - Time complexity of operations in a Linked List:
      - Accessing: O(n) - This requires us to traverse over the LL.
      - Searching: O(n) - This also requires us to traverse the LL.
      - Insertion: O(1) - This can be constant time if we know the node we are inserting at, else it is O(n).
      - Deletion: O(1) - This can be constant time if we know the node we are inserting at, else it is O(n).
  """

