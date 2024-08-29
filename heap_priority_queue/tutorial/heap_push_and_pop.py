"""
By using Heaps we can read the minimum or maximum value in constant time O(1). However pushing and popping to a heap
is more complicated and will run in O(log-n) time.

Pushing:
  - As heaps are a contiguous, we add the new value we are pushing at the last index.
  - We then check the newly added values parent, and compare if it is smaller or bigger than the parent value.
    - In the case of a min heap, if the newly added node is smaller than the parent, we swap.
    - In the case of a max heap, if the newly added node is bigger than the parent, we swap.
  - The process of swapping with the parent is called percolating up.
"""
class Heap:
  def __init__(self):
    self.heap[0]

  def push(self, val):
    self.heap.append(val)
    i = len(self.heap) - 1

    # Percolate up
    while i > 1 and self.heap[i] < self.heap[i // 2]:
      temp = self.heap[i]
      self.heap[i] = self.heap[i // 2]
      self.heap[i // 2] = temp
      i = i // 2
  """
  Popping:
  Removing the highest priority value in a min/max heap is more complicated that simply swapping with the min or max of the child nodes.
  This is because it could violate the structure property of the heap, leaving missing nodes.

  This is the correct way to pop from a heap:
    - First we take the root node, and assign it to a separate variable, since this is what we are returning.
    - We then assign the root node the value at the last index of the heap, or the right most node if thinking of it as a binary tree.
    - Now we run checks and percolate down, checking if the value at the root node is greater than the values at the two children nodes.
    - This carries on until the nodes are in the correct positions, and the structure property has been preserved.
  """
  def pop(self):
    if len(self.heap) == 1: # First we check if the heap is only of length 1, if yes we do not have a valid heap, so return None
      return None
    if len(self.heap) == 2: # If the heap is only of length 2, then we can pop and return that value.
      return self.heap.pop()

    res = self.heap[1] # We assign the root value at index one to a variable, which we will return later.
    self.heap[1] = self.heap.pop() # Next we assign the last value in the heap, to the root node.
    i = 1 # We also create a pointer to the root node.

    while 2 * i < len(self.heap): # While there are children nodes, which we find by 2 * i.
      # Next we check if there is a right child, and if the right child is smaller than the left child, and if the parent node is greater than the right child,
      if (2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]):
        # If so, we can swap the right child and parent node, and update the pointer to the right child
        temp = self.heap[i]
        self.heap[i] = self.heap[2 * i + 1]
        self.heap[2 * i + 1] = temp
        i = 2 * i + 1
      # If the parent is greater than the left child, swap and update the pointer
      elif self.heap[i] > self.heap[2 * i]:
        temp = self.heap[i]
        self.heap[i] = self.heap[2 * i]
        self.heap[2 * i] = temp
        i = 2 * i
      # Else if there is no children, we break from the loop
      else:
        break
    # We can then return the result.
    return res
