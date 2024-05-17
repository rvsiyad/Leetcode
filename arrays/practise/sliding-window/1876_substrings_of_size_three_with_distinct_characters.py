class SubstringsOfSizeThree:
  """
  A string is good if there are no repeated characters.

  Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

  Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

  A substring is a contiguous sequence of characters in a string.

  Example:
  Input: s = "xyzzaz"
  Output: 1
  Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
  The only good substring of length 3 is "xyz".
  """

  def countGoodSubstrings(s):
    if len(s) < 3: return 0

    count = 0
    sCount = {}

    # check first 3 characters of the string
    # Loop through len of 3 of s,
    for i in range(3):
      sCount[s[i]] = 1 + sCount.get(s[i], 0) # add to a hashmap, setting value to 0 if first time or + 1 if already present

    # If mapLength == 3, count +=1
    if len(sCount) == 3: count += 1
    # Left pointer set to 0
    L = 0
    # Loop from 3, to len of s, R pointer
    for R in range(3, len(s)):
      sCount[s[R]] + 1 + sCount.get(s[R], 0)  # Increment value on the right
      sCount[s[L]] -= 1 # Decrement value on the left

      # Remove left pointer if 0:
      if sCount[s[L]] == 0:
          sCount.pop(s[L])

    # If mapLength == 3, count +=1
      if len(sCount) == 3: count += 1

    # Increment L pointer
      L += 1

    # return Count
    return count

"""
Time complexity:
This solution is O(n) time complexity, as there are no nested for loops and reading and writing to the hashmaps are O(1) time.
"""