from lc import *

# https://leetcode.com/problems/word-search-ii/discuss/2783455/Python-3-one-line

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board = {i+j*1j: c for i, row in enumerate(board) for j, c in enumerate(row)}
        res, trie = [], (Trie:=lambda: defaultdict(Trie))()
        any(setitem(reduce(dict.__getitem__,w,trie),'$',w) for w in words)
        def dfs(z, parent):
            if not (c:=board.get(z)) in parent:
                return
            if (word:=(node:=parent[c]).pop('$', None)):
                res.append(word)
            board[z] = None
            any(dfs(z+1j**k, node) for k in range(4))
            board[z] = c
            if not node:
                parent.pop(c)
        any(dfs(z, trie) for z in board)
        return res

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return ([b:={i+j*1j: c for i, row in enumerate(board) for j, c in enumerate(row)}, r:=[],
            t:=(T:=lambda: defaultdict(T))(), [setitem(reduce(dict.__getitem__, w, t),'$',w) for w in words],
            (f:=lambda z,p: (c:=b.get(z)) in p and (((w:=(n:=p[c]).pop('$',0)) and r.append(w))
            or ((setitem(b,z,0) or [f(z+1j**k, n) for k in range(4)] and setitem(b,z,c))
            or (n or p.pop(c)))))] and [f(z,t) for z in b] and r)

test('''
212. Word Search II
Hard

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
''', sort=True)
