from lc import *

# https://leetcode.com/problems/as-far-from-land-as-possible/discuss/360960/Python-BFS/822409

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        land = {(i, j) for i, j in product(range(n), range(n)) if grid[i][j]}
        water = {(i, j) for i, j in product(range(n), range(n)) if not grid[i][j]}
        while water:
            if not land: return -1
            land = {(x, y) for i, j in land for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if (x, y) in water}
            water -= land
            res += 1
        return res or -1

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        d,c = 0,lambda t:{i+j*1j for i,r in enumerate(grid) for j,x in enumerate(r) if x==t}
        water, land = c(1), c(0)
        while water and land:
            water = {t for z in water for t in (z+1j**k for k in range(4)) if t in land}
            land -= water
            d += 1
        return d or -1

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        return next((d or -1 for _ in count() if not(a and b and (a:={t for z in a for t in (z+1j**k for k in range(4)) if t in b},b:=b-a,d:=d+1))),(d:=0,a:=(c:=lambda t:{i+j*1j for i,r in enumerate(grid) for j,x in enumerate(r) if x==t})(1),b:=c(0)))

test('''

1162. As Far from Land as Possible
Medium

2619

75

Add to List

Share
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Example 3:

Input: grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output: -1

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
''')
