"""
Difficulty: Medium

Question:
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
Word may contain dots '.' where dots can be matched with any letter.
"""
class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = False

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    curr.word = True

# ^^^^^^^^^^^^^^^^^^^^^ All previous code is things i am familiar with ^^^^^^^^^^^^^^^^^^^^^^^^^^^

  def search(self, word): # To find a word in a trie and also including a wildcard where "." is considered any value, we can search each trie path using dfs
    def dfs (j, root): # We create our dfs helper which takes in an index and the node we are at
      curr = root # We create a pointer for the root called curr
      for i in range(j, len(word)): # Loop through the length of the word, we use the j index to show where we still need to evaluate our string from
        if word[i] == ".": # If the word at index i is the "." wildcard
          for child in curr.children.values(): # We want to iterate over all children of the curr node and run the dfs function recursively
            if dfs(i + 1, child): # If the dfs helper returns true, we can return true
              return True
          return False # Else if no paths match across all children, we return False

        else: # If the curr value is not the "." wildcard we search a trie data structure as normal
          if word[i] not in curr.children: # If the current word is not one of the children
            return False # Return false
        curr = curr.children[word[i]] # Update curr to be the next TrieNode
      return curr.word # Return if that path is an actual word inserted.
    return dfs(0, self.root) # Return the DFS function, passing in the starting pointer of 0 and the root of the Trie

  # This is not part of the question, just practice
  # To print all the words, we must go down each path in the trie and print each word we see where its node is true
  def printAllWords(self):
    def dfs(node, prefix):
      curr = node
      if curr.word:
        print(prefix)
      for char, child in curr.children.items():
        dfs(child, prefix + char)

    dfs(self.root, "")

example = WordDictionary()

example.addWord("bad")
example.addWord("dad")
example.addWord("mad")
example.search("pad")
example.search("bad")
example.search(".ad")
example.search("b..")
example.printAllWords()
