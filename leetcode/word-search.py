from lc import *

# https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        m,n = len(b),len(b[0])
        def f(i,j,w):
            if not w:
                return True
            if  m>i>=0<=j<n and w[0]==b[i][j]:
                t = b[i][j]
                setitem(b[i],j,'$')
                r = any(map(f,(i+1,i-1,i,i),(j,j,j+1,j-1),[w[1:]]*4))
                setitem(b[i],j,t)
                return r
        return any(f(i,j,w)for i in range(m)for j in range(n))

class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        m,n=len(b),len(b[0]);f=lambda i,j,w:not w or m>i>=0<=j<n and w[0]==b[i][j]and(t:=b[i][j],setitem(b[i],j,'$'),r:=any(map(f,(i+1,i-1,i,i),(j,j,j+1,j-1),[w[1:]]*4)),setitem(b[i],j,t))and r;return any(f(i,j,w)for i in range(m)for j in range(n))

test('''
79. Word Search
Medium

14878

615

Add to List

Share
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

Accepted
1,462,871
Submissions
3,549,706
''')
