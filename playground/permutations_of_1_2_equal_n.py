def combinationsOf1_2_equal(n):
  result = []

  def backtrack(currentSum, combination, n):
    if currentSum > n:
      return
    
    if currentSum == n:
      result.append(combination.copy())
      return
    
    combination.append(1)
    backtrack(currentSum + 1, combination, n)

    combination.pop()
    combination.append(2)
    backtrack(currentSum + 2, combination, n)
    combination.pop()
  
  backtrack(0, [], n)
  return result

print(combinationsOf1_2_equal(3))
