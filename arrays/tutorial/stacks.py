class Stacks:
  """
  Stacks allow users to add values it, and pop from the top of the stack.

  It follows the last in in first out principle for a data structure.

  Stacks can be initialised in the same way as an array.
  """

  # How to create a stack
  stack = []

  # How to add to a stack, using the append function
  stack.append(12)
  stack.append(11)
  stack.append(110)
  stack.append(1223923)

  print(stack)

  # Use the pop function to remove from the last/top element of the stack.
  stack.pop()

  print(stack)

  # Retrieve the last value of the stack by indexing the -1 index.
  variable = stack[-1]
  print(variable)