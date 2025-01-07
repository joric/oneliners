from lc import *

# https://leetcode.com/problems/string-matching-in-an-array/solutions/6236300/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07

class Solution:

    class TrieNode:
        def __init__(self):
            # Tracks how many times this substring appears in the Trie.
            self.frequency = 0
            # Maps characters to their respective child nodes.
            self.child_nodes = {}

    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []
        root = self.TrieNode()  # Initialize the root of the Trie.

        # Insert all suffixes of each word into the Trie.
        for word in words:
            for start_index in range(len(word)):
                # Insert each suffix starting from index start_index.
                self._insert_word(root, word[start_index:])

        # Check each word to see if it exists as a substring in the Trie.
        for word in words:
            if self._is_substring(root, word):
                matching_words.append(word)

        return matching_words

    def _insert_word(self, root: "TrieNode", word: str) -> None:
        current_node = root
        for char in word:
            if char not in current_node.child_nodes:
                # Create a new node if the character does not exist.
                current_node.child_nodes[char] = self.TrieNode()
            current_node = current_node.child_nodes[char]
            current_node.frequency += 1  # Increment the frequency of the node.

    def _is_substring(self, root: "TrieNode", word: str) -> bool:
        current_node = root
        for char in word:
            # Traverse the Trie following the characters of the word.
            current_node = current_node.child_nodes[char]
        # A word is a substring if its frequency in the Trie is greater than 1.
        return current_node.frequency > 1


# https://leetcode.com/problems/string-matching-in-an-array/solutions/586046/python-3-one-line-sorted-brute-force/?envType=daily-question&envId=2025-01-07

class Solution:
  def stringMatching(self, d: List[str]) -> List[str]:
    r=range(len(d));return[d[i] for i in r if any(d[i]in d[j]for j in r if i!=j)]

# https://leetcode.com/problems/string-matching-in-an-array/solutions/5625321/one-line-solution/?envType=daily-question&envId=2025-01-07

class Solution:
    def stringMatching(self, d: List[str]) -> List[str]:
        return[a for a in d for b in d if a in b and a<b]

# https://leetcode.com/problems/string-matching-in-an-array/solutions/653782/one-line-in-python/?envType=daily-question&envId=2025-01-07

class Solution:
    def stringMatching(self, d: List[str]) -> List[str]:
        return[a for a in d if~-sum(a in b for b in d)]

test('''
1408. String Matching in an Array
Solved
Easy
Topics
Companies
Hint
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
''')
