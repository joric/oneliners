from lc import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return any(setitem(grid[i],j,grid[i][j]+(min(grid[i-1][j] if i>0 else inf, grid[i][j-1] if j>0 else inf) if i or j else 0)) for i in range(len(grid)) for j in range(len(grid[0]))) or grid[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return (n:=len(grid[0]),s:=[0]+[inf]*(n-1),[setitem(s,i,r[i]+min(s[i-1] if i else s[i],s[i])) for r in grid for i in range(n)]) and s[-1]

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
