from lc import *

# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/discuss/819303/Python-you-need-at-most-2-days

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(r, c, g):
            if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]) or g[r][c] != 1:
                return
            g[r][c] = 2
            for nr, nc in (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1):
                dfs(nr, nc, g)

        def num_of_islands(g):
            res = 0
            for r in range(len(g)):
                for c in range(len(g[0])):
                    if g[r][c] == 1:
                        dfs(r, c, g)
                        res += 1
            return res

        if num_of_islands(copy.deepcopy(grid)) != 1:
            return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    grid_copy = copy.deepcopy(grid)
                    grid_copy[r][c] = 0
                    if num_of_islands(grid_copy) != 1:
                        return 1
        return 2

class Solution:
    def minDays(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);f,e=lambda r,c,g:m>r>-1<c<n and g[r][c]==1 and (setitem(g[r],c,2),[*map(f,(r-1,r,r+1,r),(c,c+1,c,c-1),[g]*4)]),lambda g:sum(1==g[r][c]and(f(r,c,g),1)[1]for r in range(m) for c in range(n));return+(1==e(deepcopy(g))and next((1 for r in range(m) for c in range(n) if g[r][c] and(t:=deepcopy(g),setitem(t[r],c,0),e(t))[2]!=1),2))

test('''
1568. Minimum Number of Days to Disconnect Island
Hard

730

154

Add to List

Share
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.
Accepted
16,152
Submissions
35,135
''')
