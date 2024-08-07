"""
Trie's - also known as a prefix trees or peak tree - can be used to store words and group/order them via their characters. For example, words beginning with
`a` will follow the "a" subtree in the trie. This gives us several advantages over using another data structure such as being able to insert and search for words in O(1) time.
Furthermore, we can search via the prefix of a value, for instance if we have a trie which has already been created for the word `apple`, it allows us to search
for letters such as `ape` as it will follow the path of the trie created by `apple`.

Trie nodes work structurally by having each node at most having 26 children in the case of letters.
"""
# Defining the TrieNode class:
class TrieNode():
  def __init__(self):
    self.children = {} # Instances of the TrieNode class are initialised with a dictionary which will hold the letters of its children nodes.
    self.word = False # TrieNodes also have a boolean to determine if this node is the end of a word.

# Defining the Trie class:
class Trie:
  def __init__(self):
    self.root = TrieNode # The Trie class has it's root not initialised as a TrieNode.

# Inserting into a Trie:
def insert(self, word): # We create an insert function which takes in the word we want to insert as the parameter
  curr = self.root # We create a curr variable and assign it the root node
  for c in word: # For each character in the word
    if c not in curr.children: # If that character is not one of the children of the current node
      curr.children[c] = TrieNode() # We add the character as a TrieNode(), as one of the children in the current nodes children hashmap
    curr = curr.children[c] # We not assign the current variable as the just created TrieNode.
  curr.word = True # Once we finish looping through the word, we assign the last node, the current node outside the loop, to be true, indicating this trie path creates a word.

# Searching in a Trie:
def searching(self, word): # Searching also takes in the word but will return a boolean value to say if the word is in the trie or not.
  curr = self.root # We create a curr variable which points to the root of the trie
  for c in word: # For each character in the word
    if c not in curr.children: # If that word does not have a child trie node
      return False # We can immediately return false, as this means we do not have the word present in our trie.
    curr = curr.children[c] # We follow the path and assign curr to the characters trieNode
  return curr.word # Finally, we return the bool value of the word, because even if a prefix is present, when searching for a word the final character node will have the word bool as True.

# Searching for a prefix:
def startsWith(self, prefix): # Determining if a prefix exists is similar to searching. It takes in the prefix as the arguments
  curr = self.root # We assign a curr variable as a pointer to the root of the trie
  for c in prefix: # For each character in the prefix
    if c not in curr.children: # If the character is not one of the children of the current node
      return False # We can return False immediately, as the path for the prefix does not exist
    curr = curr.children[c] # We assign the current node pointer to the character child trie to continue the prefix search
  return True # Finally, different from the search, if the loop finishes we can return True as we are only looking for the prefix, not if the word is present in the trie.