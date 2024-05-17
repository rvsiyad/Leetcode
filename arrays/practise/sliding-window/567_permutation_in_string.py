class PermutationInString:
  """
  Difficulty: Medium

  Given two strings s1 and s2, return true if s2 contains a permutation of s1,
  or false otherwise.

  In other words, return true if one of s1's permutations is the substring of s2.

  Example 1:

  Input: s1 = "ab", s2 = "eidbaooo"
  Output: true
  Explanation: s2 contains one permutation of s1 ("ba").
  """

  def checkPermutation(s1, s2):
    if len(s1) > len(s2): # First we check if substring is greater than string, return false if true.
      return False

    s1Count, s2Count = {}, {} # Two hashmaps, keep count of values.

    # Loop through the length of the substring, that is our window.
    for i in range (len(s1)):
      s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0) # Add values at index i to each hashmap, increment count by 1.
      s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

    if s1Count == s2Count: # We can check the first window and see if they match, return true.
      return True

    L = 0 # Initialise a left pointer.

    # Loop from the end of the length of the substring, to the end of the string.
    for R in range (len(s1), len(s2)):
      s2Count[s2[R]] = 1 + s2Count.get(s2[R], 0) # Add the value at the right pointer.
      s2Count[s2[L]] -= 1 # Remove the value at the left pointer.

      if s2Count[s2[L]] == 0: # If the value on the left in the hashmap is 0, pop from the map.
        s2Count.pop(s2[L])

      L += 1 # Increment the left pointer up.

      if s2Count == s1Count: # Check if maps are equal, then return true.
        return True

    return False # Return false if conditions have not been met.

