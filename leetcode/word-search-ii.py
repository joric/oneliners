from lc import *

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, trie = [], (Trie:=lambda: defaultdict(Trie))()
        [reduce(dict.__getitem__, word, trie).__setitem__(None, word) for word in words]
        board = {i + j * 1j: c for i, row in enumerate(board) for j, c in enumerate(row)}
        def rm(trie, word):
            path = [trie]
            [path.append(path[-1].get(c)) for c in word]
            if not path[-1]:
                for char, parent in zip(word[::-1], path[::-1][1:]):
                    if len(parent) > 1:
                        break
                    del parent[char]
        def dfs(node, z):
            if (word:=node.pop(None, None)):
                res.append(word)
                rm(trie, word)
            tmp = board.get(z)
            if tmp in node:
                board[z] = None
                [dfs(node[tmp], z+1j**k) for k in range(4)]
                board[z] = tmp
        [dfs(trie, z) for z in board]
        return res

test('''

212. Word Search II
Hard

6981

302

Add to List

Share
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Example 3:

Input: board = [["a","b","c","e"],["z","z","d","z"],["z","z","c","z"],["z","a","b","z"]], words = ["abcdce"]
Output: ["abcdce"]

Example 4:

Input: board = [["a","a"]], words = ["aaa"]
Output: []

Example 5:

Input: board = [["a","b"],["a","a"]], words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
Output: ["aba","aaa","aaab","baa","aaba"]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

''', check=lambda res, expected, board, words: sorted(res)==sorted(expected))
