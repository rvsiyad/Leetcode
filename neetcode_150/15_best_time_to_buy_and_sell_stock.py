"""
Brute force solution:
- Create maxProfit variable
- Double for loop over the array
- update the max if profit[i] < profit[j]
- return maxProfit
"""
def brute_force_solution(prices):
  max_profit = 0

  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      if prices[i] < prices[j]:
        max_profit = max(max_profit, prices[j] - prices[i])

  return max_profit

"""
Optimised, sliding window approach:
- Create maxProfit variable
- L pointer to 0, R pointer to 1
- Update L pointer to R if prices[R] < prices[L]
- Else we take the max_profit here
- return max profit
"""
def optimised_solution(prices):
  max_profit = 0
  L = 0

  for R in range(1, len(prices)):
    if prices[R] < prices[L]:
      L = R
    else:
      max_profit = max(max_profit, (prices[R] - prices[L]))

  return max_profit