"""
Brute force approach:
- Loop over all queries and add to hashmap, adding float("inf") as the value
- Loop over start end intervals
- Loop over the query and its minLengths in hashmap.items()
- If the query is out-of-bounds of the start and end, continue
- If in range, we update the value in query hashmap to the min between itself and the difference between end and start
- Create results array
- Loop through all queries, looking for its value in the hashmap and appending to results array
- If value in hashmap is float("inf), appending -1
"""
def brute_force_solution(intervals, queries):
  query_to_length = {q:float("inf") for q in queries}

  for start, end in intervals:
    for query, minLength in query_to_length.items():
      if query < start or query > end:
        continue

      newMinLength = min(minLength, end - start + 1)
      query_to_length[query] = newMinLength

  result = []

  for q in queries:
    if query_to_length[q] == float("inf"):
      result.append(-1)
    else:
      result.append(query_to_length[q])

  return result