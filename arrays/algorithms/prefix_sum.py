"""
Prefix sum works by creating an array which holds the going sum of the array. For example, an array [2,-1,3,-3,4] will have a prefix array with the
following values [2,1,4,1,5]. This is extremely useful when we want to retrieve the sum of a subarray ending at a specific index i.

Here is a question:
Given an array of values, design a data structure that can query the sum of a subarray of the values.

Answer:
First, lets build our prefix sum class called PrefixSum, which will take an array we want to build the prefix sum array for. Using this array we
create our prefix sum array which holds the sums at each index.
"""
class PrefixSum:

  def __init__(self, nums):
    self.prefix = []
    total = 0

    for i in nums:
      total += i
      self.prefix.append(total)
  """
  After building this prefix array for the original array, we can now create another function which will return the sub of values between two
  indexes. We can do this by taking the value at our R and L - 1 (Sum of all values prior to the requested sum between the L and R) indexes in the prefix sum,
  and subtract them from each other i.e. Right - Left - 1.
  """
  def findSumBetweenRange(self, left, right):
    prefixLeft = self.prefix[left - 1] if left > 0 else 0 # Here we are checking if the L index is greater than 0, otherwise we would be looking for an out of bounds value. 
    prefixRight = self.prefix[right] # If true, we subtract 0 from the prefixRight

    return (prefixRight - prefixLeft)