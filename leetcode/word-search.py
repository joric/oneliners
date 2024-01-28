from lc import *

# https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        m,n = len(b),len(b[0])
        def f(i,j,k):
            if k==len(w):
                return True
            if  m>i>-1<j<n and w[k]==b[i][j]:
                t = b[i][j]
                b[i][j]='$'
                r = any(f(i+q,j,k+1)or f(i,j+q,k+1)for q in(-1,1))
                b[i][j]=t
                return r
        return any(f(i//n,i%n,0)for i in range(m*n))

class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        m,n=len(b),len(b[0]);return any((f:=lambda i,j,k:k==len(w)or m>i>-1<j<n and w[k]==b[i][j]and(t:=b[i][j],setitem(b[i],j,'$'),r:=any(f(i+q,j,k+1)or f(i,j+q,k+1)for q in(-1,1)),setitem(b[i],j,t))and r)(i//n,i%n,0)for i in range(m*n))

class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        # optional precalc (see https://leetcode.com/problems/word-search/discuss/4087946/These-tricks-can-make-your-code-128x-times-faster)
        c = Counter(sum(b,[]))
        for k,v in Counter(w).items():
            if c[k]<v:
                return False
        if c[w[0]]>c[w[-1]]:
             w = w[::-1]

        e=enumerate;b={i+j*1j:c for i,r in e(b)for j,c in e(r)}
        def f(z,k=0):
            if k==len(w):
                return True
            if b.get(z)==w[k]:
                b[z]=0
                r=any(f(z+1j**i,k+1)for i in range(4))
                b[z]=w[k]
                return r
        return any(map(f,b))

# borderline TLE (8s)

class Solution:
    def exist(self, b: List[List[str]], w: str) -> bool:
        e=enumerate;b={i+j*1j:c for i,r in e(b)for j,c in e(r)};return any(map((f:=lambda z,k=0:k==len(w)or b.get(z)==w[k]and(setitem(b,z,0),any(f(z+1j**i,k+1)for i in range(4)),setitem(b,z,w[k]))[1]),b))

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
 

Example 4:

Input: board = [["C","A","A"],["A","A","A"],["B","C","D"]], word = "AAB"
Output: true

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
