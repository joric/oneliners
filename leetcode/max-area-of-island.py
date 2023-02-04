#!/usr/bin/env python3

from lc import *

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + sum(map(dfs,(i+1,i,i-1,i),(j,j+1,j,j-1)))
            return 0
        return max(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))

class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        return max((f:=lambda i,j:setitem(g[i],j,0) or 1 + sum(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))
            if 0<=i<len(g) and 0<=j<len(g[0]) and g[i][j] else 0)(i,j) for i in range(len(g)) for j in range(len(g[0])))

class Solution:
    def maxAreaOfIsland(self, grid):
        grid = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        def area(z):
            return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))
        return max(map(area, set(grid)))

class Solution:
    def maxAreaOfIsland(self, grid):
        return max(map(a:=lambda z: g.pop(z, 0) and 1 + sum(a(z + 1j**k) for k in range(4)),
            set(g:= {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)})))

test('''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
''')


