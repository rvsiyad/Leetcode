"""
Difficulty: Medium

Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""
def letterCombinations(digits): # We are given a digits array
  telephone = { # We create our dict which will map the digits in the array to the letters they could be
    '2' : ["a","b","c"],
    '3' : ["d","e","f"],
    '4' : ["g","h","i"],
    '5' : ["j","k","l"],
    '6' : ["m","n","o"],
    '7' : ["p","q","r", "s"],
    '8' : ["t","u","v"],
    '9' : ["w","x","y", "z"],
  }

  res = [] # We create our empty results variable

  def helper(i, combination): # Here we are creating our helper variable which will be called recursively
    if i >= len(digits): # If the index is greater than the length of the digits, we can append the current combination to the result and return
      res.append(combination)
      return

    for c in telephone[digits[i]]: # For each character in the telephone dict that maps to the digit
      helper(i + 1, combination + c) # We can call the helper function again with the index incremented by one and adding the current character to the current combination

  helper(0, "") # We call our helper function with an index of 0 and the empty combination string
  return [] if res == [""] else res # Finally we return the result
"""
Notes:
- Similar to other backtracking problems, I am just so bad at noticing the edge cases and when to call the helper function again
- This problem calls the helper inside a for loop, adding the current character as we go.
"""