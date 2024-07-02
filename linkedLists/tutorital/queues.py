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
