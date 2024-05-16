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
    if len(p) > len(s): return []

    pCount, sCount = {}, {}

    for i in range(len(p)):
      pCount[p[i]] = 1 + pCount.get(p[i], 0)
      sCount[s[i]] = 1 + sCount.get(s[i], 0)

    res = [0] if sCount == pCount else []

    L = 0

    for R in range(len(p), len(s)):
      sCount[s[R]] = 1 + sCount.get(s[R], 0)
      sCount[s[L]] -= 1

      if sCount[s[L]] == 0:
        sCount.pop(s[L])

      L += 1

      if sCount == pCount:
        res.append(L)

    return res

  print(findAnagrams('qwertyqweerqweeqweq','qew'))