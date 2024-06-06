class ContainerWithMostWater:
  """
  Difficulty: Medium

  Question:
  You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

  Find two lines that together with the x-axis form a container, such that the container contains the most water.

  Return the maximum amount of water a container can store.

  Notice that you may not slant the container.

  Example 1:

  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
  Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

  Example 2:

  Input: height = [1,1]
  Output: 1
  """
  def maxArea(height):
    # Holds the maxArea of water
    maxArea = 0

    L = 0 # Initialise a L pointer to the start
    R = len(height) - 1 # Initialise R pointer to end of array

    # While L pointer is less than R pointer
    while L < R:
        currArea = min(height[L], height[R]) * (R - L) # Calculate the area, (height x width)
        maxArea = max(currArea, maxArea) # Set maxArea to the max between the currArea and the maxArea

        if height[L] < height[R]: # If value at L is smaller than value at R, increment L pointer up and index
            L += 1
        elif height[R] < height[L]: # If value at R pointer is smaller than value at L, decrement the R pointer
            R -= 1
        else:
            R -= 1 # If they are equal, just move one pointer

    return maxArea # Return the maxArea

