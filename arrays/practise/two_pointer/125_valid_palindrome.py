class ValidPalindrome:
  """
  Difficulty: Easy

  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
  it reads the same forward and backward. Alphanumeric characters include letters and numbers.

  Given a string s, return true if it is a palindrome, or false otherwise.

  Example:

  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.
  """
  def isPalindrome(s):
    # Here we create a helper function, which returns true if the a value is a valid number or letter.
    # It works by comparing the ASCI values, and making sure the value s is between the valid character ranges.
    def isAlphaNum(s):
      return (ord("a") <= ord(s) <= ord("z") or
              ord("A") <= ord(s) <= ord("Z") or
              ord("0") <= ord(s) <= ord("9"))

    # Here we create a empty string to hold our string minus the non-alphanumeric values.
    validString = ""

    # Loop through the length of s
    for i in range(len(s)):
        if isAlphaNum(s[i]): # If the value at s[i] is alphanumeric, it is added to the valid string
            validString += (s[i])

    # We reassign the variable to only contain lowercase letters.
    validString = validString.lower()

    # Create L and R pointer, at the start and end indexes.
    L = 0
    R = len(validString) - 1

    # While L pointer is smaller than R pointer
    while L < R:
        if validString[L] != validString[R]: # If L and R pointers are not equal, can instantly return false.
            return False

        L += 1 # Increment the L pointer
        R -= 1 # Decrement the R pointer

    return True # Return true if all values at opposite ends are equal.

  print(isPalindrome("A man, a plan, a canal: Panama"))

  """
  Time complexity:
  Since there are no nested loops, the solution runs in O(N) time.
  """