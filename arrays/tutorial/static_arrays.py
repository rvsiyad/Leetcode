class StaticArrays:
  #Creating an array in python:
  myArrayNum = [1,2,3,4,5]
  myArrayString = ['a','b','c','d','e']

  # Arrays are accessed via an index and can be printed using the print() method:
  def print_index(array):
    print(array[0]) # This will print 1.

  print_index(myArrayNum)
  print('-------------------------')

  # Arrays can be traversed over using a For loop:
  def print_via_for_loop(array):
    for i in range (len(array)):
      print(array[i])

  print_via_for_loop(myArrayString)
  print('-------------------------')

  # Or a While loop:
  def print_via_while_loop(array):
    i = 0
    while(i < len(array)):
      print(array[i])
      i += 1

  print_via_for_loop(myArrayNum)
  print('-------------------------')

  # Deleting from end of an array
  def delete_from_end(array):
    length = len(array)

    if length > 0:
      array[length - 1] = 0 # Setting an array value to 0, no value in array.

  delete_from_end(myArrayNum)
  print(myArrayNum)
  print('-------------------------')

  # Delete at the Nth index, maintaining a contiguous array:
  def delete_from_middle(array, i):
    length = len(array)

    # Loop through the array, replace the previous value with the current.
    for index in range(i + 1, length):
      array[index - 1] = array[index] # No need to remove array[i], it is being overwritten.

  delete_from_middle(myArrayNum, 0)
  print(myArrayNum)
  print('-------------------------')

  # Insertion at the end of an array:
  def insert_at_end(array, value):
    length = len(array)
    array[length - 1] = value

  insert_at_end(myArrayNum, 22)
  print(myArrayNum)
  print('-------------------------')

  # Inserting at Nth index, maintaining a contiguous array:
  def insert_in_middle(array, value, i):
    length = len(array) - 1

    for index in range(length - 1, i - 1, -1):
      array[index + 1] = array[index]

    array[i] = value
    print(array)

  newArrayNum = [1,2,3,4,5,6,7,8,9]
  insert_in_middle(newArrayNum, 33, 2)