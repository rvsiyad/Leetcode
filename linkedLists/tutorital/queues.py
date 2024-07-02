class Queues:
  """
  - Introduction:
    Queues are like a stack, except they allow us to remove from both the first and last values inputted.
    They follow the first in first out (FIFO) principle and are implemented using linked lists.

    When initialised, the head and tail are both set to the first node, however as the list starts to grow,
    the tail will follow the new nodes created. The head will be moved to the next node if we remove the
    first node.

    Queues have two common operations, enqueue and dequeue. Enqueue adds to the tail of the queue while dequeue
    removes from the front of the list.
  """
  def enqueue(self, val):
    newNode = ListNode(val) # Create a new node with the value entered.                            # type: ignore

    if self.right: # If there is already a Queue
      self.right.next = newNode # Add the node to the end of the queue
      self.right = self.right.next # Reassign the last value as the new tail.

    else: # Else we create the new Queue and assign the head and tail to the new node.
      self.left = self.right = newNode

