from lc import *

# Q3. https://leetcode.com/contest/weekly-contest-397/
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

# https://leetcode.com/problems/maximum-difference-score-in-a-grid/discuss/5146220/Easy-memoization-approach-oror-C%2B%2B

class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        h,w = len(g),len(g[0])
        @cache
        def f(x,y):
            r = -inf
            c = g[x][y]

            for i in range(x+1,h):
                a = g[i][y] - c
                r = max(r, a)
                b = f(i,y)
                if a>0 and b>0:
                    r = max(r, a+b)

            for j in range(y+1,w):
                a = g[x][j] - c
                r = max(r, a)
                b = f(x,j)
                if a>0 and b>0:
                    r = max(r, a+b)

            return r

        return max(f(i,j)for i in range(h) for j in range(w))

# https://leetcode.com/problems/maximum-difference-score-in-a-grid/discuss/5145704/JavaC%2B%2BPython-DP-Minimum-on-Top-Left

class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        r,h,w = -inf,len(g),len(g[0])
        for i in range(h):
            for j in range(w):
                p = min(g[i-1][j] if i else inf, g[i][j-1] if j else inf)
                r = max(r, g[i][j] - p)
                g[i][j] = min(g[i][j], p)
        return r

class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        return max((g[i][j]-(p:=min(i and g[i-1][j]or inf,j and g[i][j-1]or inf)),setitem(g[i],j,min(g[i][j],p)))[0]for i in range(len(g))for j in range(len(g[0])))

class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        e=enumerate;return max((v-(p:=min(i and g[i-1][j]or inf,j and g[i][j-1]or inf)),setitem(g[i],j,min(v,p)))[0]for i,r in e(g)for j,v in e(r))

test('''
3148. Maximum Difference Score in a Grid
Medium

56

10

Add to List

Share
You are given an m x n matrix grid consisting of positive integers. You can move from a cell in the matrix to any other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value c1 to a cell with the value c2 is c2 - c1.
You can start at any cell, and you have to make at least one move.

Return the maximum total score you can achieve.

 

Example 1:


Input: grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]

Output: 9

Explanation: We start at the cell (0, 1), and we perform the following moves:
- Move from the cell (0, 1) to (2, 1) with a score of 7 - 5 = 2.
- Move from the cell (2, 1) to (2, 2) with a score of 14 - 7 = 7.
The total score is 2 + 7 = 9.

Example 2:



Input: grid = [[4,3,2],[3,2,1]]

Output: -1

Explanation: We start at the cell (0, 0), and we perform one move: (0, 0) to (0, 1). The score is 3 - 4 = -1.

 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 105
Accepted
8,417
Submissions
18,785
''')
