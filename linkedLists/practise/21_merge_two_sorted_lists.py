class MergeTwoSortedLists:
  """
  Difficulty: Easy

  Question:
  You are given the heads of two sorted linked lists list1 and list2. Merge the
  two lists into one sorted list. The list should be made by splicing together the
  nodes of the first two lists. Return the head of the merged linked list.

  Example 1:
  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4,4]
  """

  def mergedTwoSortedLists(l1, l2):
    dummy = LinkedNode()  # We create a dummy node from which we can start our linked list.               # type: ignore
    curr = dummy # We set the current start point as the dummy node.

    while l1 and l2: # While list1 and list2 are not finished
      if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
      else:
        curr.next = l2
        l2 = l2.next

      curr = curr.next

    if l1:
      curr.next = l1
    else:
      curr.next = l2

    return dummy.next