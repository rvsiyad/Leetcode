class LongestSubstringWithoutRepeatingCharacters:
  """
  Difficulty: Medium

  Given a string s, find the length of the longest substring without repeating characters.

  Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
  """
  def lengthOfLongestSubstring(s):
    # Initialise a maxLength
    maxLength = 0
    # Initialise a hashMap to keep count
    sCount = {}

    # Initilise a L pointer
    L = 0
    # Loop through the length of the string
    for R in range(len(s)):
        # Add the R pointer value to the hashMap
        sCount[s[R]] = 1 + sCount.get(s[R], 0)

        # While the max(hashmap.Value()) > 1:
        while max(sCount.values()) > 1:
            # Remove the value at the L pointer
            sCount[s[L]] -= 1
            # Increment the L pointer up
            L += 1

        # Take the max between currentMax(R - L + 1) and maxLength
        maxLength = max(R - L + 1, maxLength)

    # Return the maxLength
    return maxLength

  print(lengthOfLongestSubstring('ABCABCDBABHBAB'))

