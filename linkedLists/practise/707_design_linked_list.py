"""
Difficulty: Medium

Question:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the
current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list,
you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in
the linked list are 0-indexed.

Implement the MyLinkedList class:

- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index'th node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
  the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the index'th node in the linked list. If index equals
  the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length,
  the node will not be inserted.
- void deleteAtIndex(int index) Delete the index'th node in the linked list, if the index is valid.
"""
class ListNode: # Add a the ListNode class from which we can create our nodes.
  def __init__(self, val):
    self.val = val # Each node, can be created with a value,
    self.prev = None # A pointer to the previous node,
    self.next = None # And a pointer to the next node.


class MyLinkedList:
  def __init__(self): # Here we are creating the constructor for the Linked List class.
    self.left = ListNode(0) # When a Linked List is called, it is initialised with both the left and right dummy nodes.
    self.right = ListNode(0)
    self.left.next = self.right # We also add the left pointers next pointer as the right pointer
    self.right.prev = self.left # And the right pointers previous node as the left pointer

    # When called, MyLinkedList will create this:
    # [left] -> <- [right] A LL with dummy nodes pointing at each other.

  def get(self, index: int) -> int: # The get function gets the value of the pointer at the index.
    curr = self.left.next # We set curr to the start of the LL by using the left dummy node.

    while curr and index > 0: # While curr is not null and the index is greater than 0 (we will decrement the index).
      curr = curr.next # Update the curr to the next node
      index -= 1 # Decrement the index on each loop, we will be at the desired loop when index == 0.

    if curr and curr != self.right and index == 0: # If there is a cur and is it not the right dummy, and we are sure index is 0.
      return curr.val # We can return the value of the current node.

    return -1 # Else we return -1.

  def addAtHead(self, val: int) -> None: # The add at head method, adds a node at the start of the LL.
    node = ListNode(val) # We create a new node with the request value.
    prev = self.left # We set prev value which holds the location of the left dummy.
    next = self.left.next # We also set a next value which holds the node next to the left dummy.

    node.next, node.prev = next, prev # We set the new nodes next and prev to what the left dummy was pointing to and the dummy node itself.
    next.prev = node # We set the next nodes previous to the new node.
    prev.next = node # We set the left dummy's next to the new node.

  def addAtTail(self, val: int) -> None: # The add at tail is similar but we add after the tail instead of the head.
    node = ListNode(val)
    prev = self.right.prev
    next = self.right

    node.next = self

  def addAtIndex(self, index: int, val: int) -> None:
      

  def deleteAtIndex(self, index: int) -> None: