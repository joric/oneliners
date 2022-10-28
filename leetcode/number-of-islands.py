from lc import *

class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(dfs,(i-1,i,i+1,i),(j,j-1,j,j+1)))
        return sum(grid[i][j] == '1' and not dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = {i + j*1j:int(val) for i,row in enumerate(grid) for j,val in enumerate(row)}
        def area(z):
            return grid.pop(z,0) and bool([area(z + 1j**k) for k in range(4)])
        return sum(map(area, set(grid)))

class Solution:
    def numIslands(self, grid):
        return sum(map(a:=lambda z:g.pop(z,0) and bool([a(z + 1j**k) for k in range(4)]),
            set(g:={i + j*1j:int(x) for i,row in enumerate(grid) for j,x in enumerate(row)})))

test('''
200. Number of Islands
Medium

17623

404

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Example 3:

Input: grid = [["1","1","1"],["0","1","0"],["0","1","0"]]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
''')
