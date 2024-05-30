class LongestRepeatingCharacterReplacement:
  """
  Difficulty: Medium

  You are given a string s and an integer k. You can choose any character of the string
  and change it to any other uppercase English character. You can perform this operation
  at most k times.

  Return the length of the longest substring containing the same letter you can get after
  performing the above operations.

  Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.
  """
  def characterReplacement(s, k):
    # Initialise a variable to keep count of max length
    maxLength = 0
    # Initialise a hashmap
    sCount = {}

    # Left pointer
    L = 0

    # Loop through string s
    for R in range(len(s)):
        # Add R pointer value to hashmap
        sCount[s[R]] = 1 + sCount.get(s[R], 0)

        # While the window length - max value in the hashmap is greater than k
        while (R - L + 1) - max(sCount.values()) > k:
            # Remove value from the Left
            sCount[s[L]] -= 1
            # Increment the Left pointer up
            L += 1

        # Reassign max length to greater between the currentMax length and the current window
        maxLength = max(R - L + 1, maxLength)

    # Return the max length
    return maxLength

