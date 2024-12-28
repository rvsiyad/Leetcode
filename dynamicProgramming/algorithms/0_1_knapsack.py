"""
The scenario behind the 0/1 knapsack is from maximising profits from items with weights so as to pick the max number of items that knapsack can hold.
Initially, the approach may be a greedy algorithm, however we might not get the max profit due to the capacity bottle neck.

The next approach is to go over each element and see the max profit we can create from assigning items based on their weight.
We can chose to either include the item or exclude it, this is very similar to a recursive backtracking approach without the popping.
It is also possible to later add caching to the solution to further reduce the time complexity to o(n * m)

Here is the brute force solution without adding caching optimisation:
"""
def bruteForce(profit, weight, capacity):
  def helper(i, profit, weight, capacity):
    if i >= len(weight):
      return 0

    skipProfit = helper(i + 1, profit, weight, capacity)

    maxProfit = skipProfit

    newCapacity = capacity - weight[i]

    if newCapacity >= 0:
      newProfit = profit[i] + helper(i + 1, profit, weight, newCapacity)

      maxProfit = max(maxProfit, newProfit)

    return maxProfit

  return helper(0, profit, weight, capacity)
"""
We add caching to this by storing the current index and the remaining capacity left. This will return us the maxProfit if we choose to include
the current item or not.
"""
def optimisation(profit, weight, capacity):
  # We create a memoization helper, this differs to the BF by adding caching
  def memoization(i, profit, weight, capacity, cache):
    # If the index is out of bounds, we return 0
    if i >= len(profit):
      return 0

    # If the cache contains the max profit for this already, we can return its saved value
    if (i, capacity) in cache:
      return cache[(i, capacity)]

    # Call the function again, skipping this profit, and save to the cache
    cache[(i, capacity)] = memoization(i + 1, profit, weight, capacity, cache)

    # Check if the new capacity is greater or equal to 0, then we are still within budget to add the profit
    newCap = capacity - weight[i]
    if newCap >= 0:
      # Check if adding the new profit is greater than skipping, if so we update the cache with the max between skipping and taking profit
      cache[(i, capacity)] = max(cache[(i, capacity)], profit[i] + memoization(i + 1, profit, weight, newCap, cache))

    # Return the maxProfit between both routes
    return cache[(i, capacity)]

  # Call the function with the empty cache hashmap
  return memoization(0, profit, weight, capacity, {})

print(optimisation([1,2,3,4,5], [2,3,4,5,3], 8))


