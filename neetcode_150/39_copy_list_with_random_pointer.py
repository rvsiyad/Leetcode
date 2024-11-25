"""
Optimised solution:
- Create a dict to hold link between curr node and the new copy
- Second loop we link the oldNode and connect the next and random pointers using the oldNode as the key
- Return the new head by using the old head as the key.
"""
class Node:
  def __init__(self, val=0, next=None, random=None):
    self.val = val
    self.next = next
    self.random = random
from collections import defaultdict

def optimised_solution(head):
  oldToCopy = {None:None}

  curr = head

  while curr:
    copy = Node(curr.val)
    oldToCopy[curr] = copy
    curr = curr.next

  curr = head

  while curr:
    copy = oldToCopy[curr]
    copy.next = oldToCopy[curr.next]
    copy.random = oldToCopy[curr.random]
    curr = curr.next

  return oldToCopy[head]