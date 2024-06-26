class FizzBuzz:
  def printFizzBuzz(n):
    for i in range(1, n):
      if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
      elif i % 5 == 0:
        print("Buzz")
      elif i % 3 == 0:
        print("Fizz")
      else:
        print(i)

  printFizzBuzz(30)

  # Can't believe you'd struggle with this at FDM! LOLZ.