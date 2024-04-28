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
