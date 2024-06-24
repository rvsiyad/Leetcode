class Slicing:
  # To slice an array in python can be done by using [:].
  # This works as follows:
  #   [initial : end] or [initial : end : jump]

  # An index is placed in initial or end. This is the range of the list from start index 0 to end of the list.
  # The jump portion of the slice is used to skip, so 2 placed in the jump means every other value, 3 would mean every 3rd value.

  arr = [0,1,2,3,4,5,6,7,8,9,10]

  # Here lets start to print the first 5 values, here we specify from index 0 to 5 = 5 values.
  # Although counting from 0 to 5 would be 6, the 5th index is not included.
  print(arr[0:5])

  # We can also do this without specifying the start index of 0. This is a shorthand technique.
  print(arr[:5])

  # Here is how to print only from the 3rd index to the 8th
  print(arr[3:9])

  # Here we can print every other value in the array using jump. Skips every other index.
  print(arr[::2])

  # Here is how a list can be put into reverse order.
  print(arr[::-1])

