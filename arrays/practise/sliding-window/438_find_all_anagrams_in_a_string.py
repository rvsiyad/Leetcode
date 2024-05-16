class FindAllAnagramsInString:
  """
  Given two strings s and p, return an array of all the start indices of p's anagrams in s.
  You may return the answer in any order.

  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Example 1:
  Input: s = "cbaebabacd", p = "abc"
  Output: [0,6]

  Explanation:
  The substring with start index = 0 is "cba", which is an anagram of "abc".
  The substring with start index = 6 is "bac", which is an anagram of "abc".
  """

  def findAnagrams(s, p):
    # Check if substring is bigger than the string we are checking. If true return empty array.
    if len(p) > len(s): return []

    pCount, sCount = {}, {} # Create one hashmap for the substring and another for the string.

    #Loop through the length of the substring
    for i in range(len(p)):
      pCount[p[i]] = 1 + pCount.get(p[i], 0) # Assign the values of the p[i] as the key, and 1 as the value.
      sCount[s[i]] = 1 + sCount.get(s[i], 0) # Assign the values of the s[i] as the key, and 1 as the value.

    res = [0] if sCount == pCount else [] # If sCount and pCount hashmaps are equal, initialise a result array to index [0], else initialise an empty result array.

    L = 0 # Create a left pointer for index 0

    # Loop starting from the length of the substring to the end of the string.
    for R in range(len(p), len(s)):
      sCount[s[R]] = 1 + sCount.get(s[R], 0) # Add the value at the R pointer index.
      sCount[s[L]] -= 1 # Subtract the value at the L pointer index.

      if sCount[s[L]] == 0: # Pop the left pointer value if equals 0
        sCount.pop(s[L])

      L += 1 # Shift left pointer by 1

      if sCount == pCount: # If hashmaps are equal, append the index of the L pointer to the result.
        res.append(L)

    return res # Return the result.

  print(findAnagrams('qwertyqweerqweeqweq','qew'))