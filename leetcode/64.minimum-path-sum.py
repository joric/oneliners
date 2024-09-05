from lc import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])        
        dp = [[0]*col for _ in range(row)]        
        dp[0][0] = grid[0][0]
        for r in range(1,row): dp[r][0] = dp[r-1][0] + grid[r][0]
        for c in range(1,col): dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1,row):
            for c in range(1,col):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        return dp[row-1][col-1]

class Solution:
    def minPathSum(self, grid):
        cost = [inf]*len(grid[0])
        for i in range(len(grid)):
            cost[0] = grid[i][0] + cost[0] if i > 0 else grid[i][0]
            for j in range(1, len(grid[0])):
                cost[j] = min(cost[j-1], cost[j]) + grid[i][j]
        return cost[-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @functools.lru_cache(None)
        def recurse(i, j):
            if i == m-1 and j == n-1: return grid[i][j]
            try:
                return grid[i][j] + min(recurse(i+1, j), recurse(i, j+1))
            except:
                return float('inf')
        return recurse(0, 0)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 0 if i==0 and j==0 else min(grid[i-1][j] if i>0 else inf, grid[i][j-1] if j>0 else inf);
        return grid[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += min(r,grid[i-1][j]) if i else r
                r = grid[i][j]
        return r

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def fn(a,b):
            print(a,b)
            i,j = b
            grid[i][j] += min(a,grid[i-1][j]) if i else a
            a = grid[i][j]
            return a
        return reduce(fn, product(range(len(grid)), range(len(grid[0]))), 0)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return reduce(lambda a,b:setitem(grid[b[0]],b[1], grid[b[0]][b[1]]+(min(a, grid[b[0]-1][b[1]]) if b[0] else a)) or grid[b[0]][b[1]],product(range(len(grid)),range(len(grid[0]))),0)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return any(setitem(grid[i],j,grid[i][j]+(min(grid[i-1][j] if i>0 else inf, grid[i][j-1] if j>0 else inf) if i or j else 0)) for i in range(len(grid)) for j in range(len(grid[0]))) or grid[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return (n:=len(grid[0]),s:=[0]+[inf]*(n-1),[setitem(s,i,r[i]+min(s[i-1] if i else s[i],s[i])) for r in grid for i in range(n)]) and s[-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return (f:=cache(lambda i,j:i|j<0 and inf or grid[i][j]+(i|j and min(f(i,j-1),f(i-1,j)))))(len(grid)-1,len(grid[0])-1)

test('''
64. Minimum Path Sum
Medium

9735

126

Add to List

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

Accepted
863,105
Submissions
1,411,676
''')