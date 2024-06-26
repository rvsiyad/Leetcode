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
