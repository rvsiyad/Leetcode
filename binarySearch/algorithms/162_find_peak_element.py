"""
Finding the peak of an unsorted array can be done using binary search. This is because if we check the values on either side and they are smaller than the
value at the m index, this is by definition a peak. If this is not the case, we check which side has the larger value on either side of the m index value.

This works as if we go towards the side which is higher, then we are guaranteed a peak. This is peak, if the slope keeps increasing (the values towards the left
are constantly increasing), then at some point there will be a smaller value. The ends of the array count as -infinity or None, meaning as long as the last or first
elements are larger than its neighbor, it is a peak.
"""
def findThePeak(arr): # We set up the problem using the usual binary search format, creating pointers for the L and R side of the arrays.
  L = 0
  R = len(arr) - 1

  while L <= R: # The loop ends if L is greater than R or if we find a peak
    m = (L + R) // 2 # Each iteration we count our middle point

    if m >= 0 and arr[m] <= arr[m - 1]: # If the value on the left of the middle is greater, half the array and remove the right sided values.
      R = m - 1
    elif m <= len(arr) - 1 and arr[m] <= arr[m + 1]: # If the value on the right of the middle is greater, half the array and remove the left sided values.
      L = m + 1
    else:
      return m # If the m value is greater than the neighboring values, return the index.

print(findThePeak([10, 20, 15, 2, 23, 90, 67]))