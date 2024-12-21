"""
Optimised approach:
- Decoding:
  - We create a single empty string called res = ""
  - We loop through the strings
  - Append the length of the string as a string, the "#" as a delimiter and the string to the result string
  - We return the resultant string
- Encoding:
- We create a res array[]
- We initialise a pointer (i) to zero.
- While i < len(s)
- We create another pointer called j, this will be incremented as long as it has not reached the "#" delimiter.
- Once the loop ends, we use the j to get the length of the string by splicing. [i:j]. Convert string number to an int.
- Once we have the length, we can use that to get the word
- i = j + 1 to pass over the delimiter #, j = i + length_of_word
- Splice the string from [i:j]
- i now equals j
"""
class OptimalSolution:
  def encode(self, strs):
    res = ""

    for s in strs:
      res += str(len(s)) + "#" + s

    return res

  def decode(self, string):
    res, i = [], 0

    while i < len(string):
      j = i

      while string[j] != "#":
        j += 1

      length_of_string = int(string[i :j])

      i =  j + 1
      j = i + length_of_string

      res.append(string[i:j])

      i = j

    return res