def findLongestSubArrayOfZeros(arr):
  # We are given an array, we can use the sliding window approach.
  # We can initialise a L pointer at index 0.
  L = 0
  # Create a total variable which holds the total currSum.
  total = 0
  # maxLength which will hold the maxLength of the longest chain of zeros.
  maxLength = 0
  # Loop through using a forloop in the range of the len of the array, call the index pointer R
  for R in range(len(arr)):
    # Add the R pointer value to the total
    total += arr[R]
    # while total > 0
    while total > 0:
      # subtract arr[L] from the total,
      total -= arr[L]
      # increment the L pointer
      L += 1
    # After the loop, take the maxLength and get the max between itself and the R - L + 1
    maxLength = max(maxLength, R - L + 1)
  # Return the maxLength.
  return maxLength

print(findLongestSubArrayOfZeros([0,0,0,0,0,0,0,0,0,0,0,0]))