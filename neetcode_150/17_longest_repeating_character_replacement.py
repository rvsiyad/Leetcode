"""
Brute force solution:
- Create a res variable
- Loop through the string
- Create a dict and a maxFreq variable
- Loop through from i to end of s
- Update the dict and keep check of the update maxFreq between itself and s[j]
- Checks for updating res, if length of string - maxF <= k
- Return res
"""
def brute_force_solution(s, k):
  res = 0

  for i in range(len(s)):
    count, maxFreq = {}, 0
    for j in range(i, len(s)):
      count[s[j]] = 1 + count.get(s[j], 0)
      maxFreq = max(maxFreq, s[j])

      if (j - i + 1) - maxFreq <= k:
        res = max(res, maxFreq)

  return res

"""
Optimised solution sliding window:
- Create a dict and a res variable
- Create a L pointer at 0
- Loop through with R, the entire string
- Add values at R pointer to count
- If length of window - max value in the count dict > k
- then we reduce the window size by removing s[l] from dict and incrementing l pointer
- Update the res to max between itself and the current window size.
"""
def optimal_solution(s, k):
  res, count = 0, {}

  L = 0

  for R in range(len(s)):
    count[s[R]] = 1 + count.get(s[R], 0)

    while (R - L + 1) - max(count.values()) > k:
      count[s[L]] -= 1
      L += 1

    res = max(res, R - L + 1)

  return res