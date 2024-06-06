class TwoSumII:
  """
  Difficulty: Medium

  Question:
  Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
  Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

  Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

  The tests are generated such that there is exactly one solution. You may not use the same element twice.

  Your solution must use only constant extra space.

  Example:

  Input: numbers = [2,7,11,15], target = 9
  Output: [1,2]
  Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
  """

  def twoSum(numbers, target):
    # Create a L and R pointer for the start and end indexes.
    L = 0
    R = len(numbers) - 1

    # While L pointer is smaller than R pointer
    while L < R:
        total = numbers[L] + numbers[R] # Create a total variable which is the addition of the L and R pointer values

        if total < target: # If the total is smaller than the target, increment the L pointer.
            L += 1

        if total > target: # If the total is greater than the target, decrement the R pointer.
            R -= 1

        if total == target: # If the total is equal to the target, return the indexes for the L and R pointers, adding 1 to each as this is a 1 indexed array.
            return [L+1, R+1]

    return []

  """
  Explanation:
  The reason this works is as the array of numbers is sorted, smallest to largest, we know the values on the right are the largest and the values on the left are smallest.

  If the total is smaller than the target value, we can simply increment the L pointer up, as that will increase the total.

  If the total is greater than the target, we can decrease the total by decrementing the R pointer down.

  Time complexity:
  As we have no nested loops, the solution runs in O(N) time.
  """