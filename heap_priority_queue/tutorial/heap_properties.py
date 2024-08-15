"""
Heaps are a specialised data structure which is implemented using a data structure called a priority queue - sometimes called a heap.
Unlike a normal queue which operate with the first in first out principle, values are removed based on a specific priority.

There are two hypes of heaps:
1. Min Heap
  - They have the smallest value at the root node. The smallest value has the highest priority to be removed.
  - All children of the root node are larger than the parent node.
2. Max Heap
  - They have the largest value at the root node. This largest value has the highest priority to be removed.
  - All children of the root node are smaller than the parent node.

Heap properties:
  Structure:
    - A binary heap is a binary tree that is a complete binary tree, where every level in the BT is full expect for the last level, which is filled
    from left to right.

  Order:
    - The order property for a min-heap is that all descendants should be greater than their ancestors. In other words, if we have a parent node,
    all children left and right, should be greater. This is recursive.
    - The order property for a max-heap is that all descendants should be smaller than their ancestors. In other words, if we have a parent node,
    all children left and right, should be smaller. This is recursive.

Although heaps are drawn using binary trees, under the hood they are implemented using arrays.

We take an array of size n + 1 where n is the number of nodes in the binary heap. We start filling the array from index 1. We fill the array from
left to right, in the same order as a bread-first search.

The reason behind filling from index 1 is to aid in finding the index at which the nodes left and right child or even the parent nodes resides.
As binary heaps are complete binary trees (again except for possibly the last level) no space is required for pointers. Instead the left and right child
and parent are calculated using formulas.

Formulas:
  - Finding Left child: 2 * i
  - Finding Right child: 2 * i + 1
  - Finding the parent: i / 2

Implementation for heap:
"""
class Heap:
  def __init__(self):
    self.heap[0]
