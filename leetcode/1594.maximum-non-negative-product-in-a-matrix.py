from lc import *

# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/solutions/856011/python-in-9-short-lines-by-daciuk-i0e8/?envType=daily-question&envId=2026-03-23

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @lru_cache(None)
        def f(i,j):
            if not (0 <= i < m and 0 <= j < n): return None, None
            cur = grid[i][j]
            if i==m-1 and j==n-1: return cur,cur
            futures = [v*cur for v in [*f(i+1,j), *f(i,j+1)] if v!= None]
            return min(futures), max(futures)
        return f(0,0)[1]%(10**9+7) if f(0,0)[1] >= 0 else -1

class Solution:
    def maxProductPath(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0])
        @cache
        def f(i,j):
            if not (0 <= i < m and 0 <= j < n):
                return None, None
            c = g[i][j]
            if i==m-1 and j==n-1:
                return c,c
            r = [v*c for v in [*f(i+1,j), *f(i,j+1)] if v!= None]
            return min(r), max(r)
        return (-1,(t:=f(0,0)[1])%(10**9+7))[t>=0]

class Solution:
    def maxProductPath(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);f=cache(lambda i,j:m>i>-1<j<n and((c,c)if[c:=g[i][j]]and i==m-1 and j==n-1 else(min(r:=[v*c for v in[*f(i+1,j),*f(i,j+1)]if v!=None]),max(r)))or(None,None));return(-1,(t:=f(0,0)[1])%(10**9+7))[t>=0]

class Solution:
    def maxProductPath(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);f=cache(lambda i,j:i<m and j<n and[c:=g[i][j]]and((c,c)if(i,j)==(m-1,n-1)else(min(r:=[v*c for v in f(i+1,j)+f(i,j+1)]),max(r)))or());return((t:=f(0,0)[1])%(10**9+7),-1)[t<0]

class Solution:
    def maxProductPath(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);f=cache(lambda i,j:i<m and j<n and[c:=g[i][j]]and((c,c)if m+n-i-j<3 else(min(r:=[v*c for v in f(i+1,j)+f(i,j+1)]),max(r)))or());t=f(0,0)[1];return(t%(10**9+7),-1)[t<0]

test('''
1594. Maximum Non Negative Product in a Matrix
Medium
Topics
premium lock icon
Companies
Hint
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
Example 3:


Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).

Other examples:

Input: grid = [[-1,1,-2,-1],[3,-3,-2,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
32,366/90.4K
Acceptance Rate
35.8%
Topics
Staff
Array
Dynamic Programming
Matrix
Weekly Contest 207
icon
Companies
Hint 1
Use Dynamic programming. Keep the highest value and lowest value you can achieve up to a point.
''')
