"""
In Breadth-First-Search (BFS), we prioritize breadth. This means we go from level to level from
left to right instead of going straight to the leaf nodes like in DFS. BFS is also known as
level-order traversal since we are in-essence moving from level to level.

In general, BFS is implemented iteratively as it cannot be done well with recursion like DFS.
To allow us to complete this, we use a queue (or a dequeue in python) as it allows us to remove
and add elements in O(1).
"""
from collections import deque # queues are implemented using a data structure called a deque in python

def bfs(root): # Our BFS method takes in the root node as one of its arguments
  queue = deque() # Initialise our queue using the deque collection we imported

  if root: # If there is a root - meaning it is not null
    queue.append(root) # We append the root to the queue - the actual root not it's value, since we will be using it as a pointer

  level = 0 # We can keep track of the level of our tree by initializing a level variable outside the loop and incrementing it
  while len(queue) > 0: # While then length of the queue is greater than 0, meaning we have a non empty queue.
    print("level: ", level) # Print the level
    for i in range(len(queue)): # Iterate over the number of values in the queue
      curr = queue.popleft() # We pop from the left of the queue which is our current node

      print(curr.val) # We can print the current nodes value, or other operation per question requirements
      if curr.left: # If the current node has a left child,
        queue.append(curr.left) # Add the child to the queue
      if curr.right: # If the current node has a right child,
        queue.append(curr.right) # Add the child to the queue
    level += 1 # Increment the level outside the for loop.
# The loops will finish once the queue is empty meaning no more nodes remain.
"""
Time and Space complexity:
Traversing over a tree using BFS means we visit each node once, regardless of the nested loops.
This means it runs in O(n) time complexity.
The Space complexity is also O(n) since each node must be stored in the queue once.
"""