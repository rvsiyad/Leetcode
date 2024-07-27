"""
Binary search over a range can be used to solve this problem. The problem is asking us to find the min amount of bananas eaten per hour speed is needed
to eat all bananas. To do this, we can create another function which will use that number to check hour long it takes for us to eat all the bananas and
returns True if we can eat all the bananas or False if we cannot.

Question:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour. Koko likes to eat slowly but
still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""
import math

def minEatingSpeed(piles, h):
  # Create our helper function which we call to see if the current speed is enough
  def canEatAllBananas(piles, h, speed):
    time = 0
    for i in piles:
      time += math.ceil(i/speed)

    return time <= h

  # Create a low and high for the min and max speeds needed to eat all the bananas
  low, high = 1, max(piles)

  while low <= high:
    m = (low + high) // 2

    if canEatAllBananas(piles, h, m):
      high = m - 1
    else:
      low = m + 1

  return low

print(minEatingSpeed([3,6,7,11], 8))