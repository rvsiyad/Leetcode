"""
Quick sort works by picking an index, using that value as the pivot value and partitioning the array into two sides where everything on the left is less than or
equal to the pivot value and everything on the right is greater than the pivot value.

The pivot value within merge sort can also be optimized by picking different pivot values. Some implementations call to pick the first index, some the middle, and
other the median between the first, middle and last indexes. Most examples stick with just using the last index as the pivot value.

The sorting occurs in place, which means it does not create any extra space - unlike with merge sort.
"""
