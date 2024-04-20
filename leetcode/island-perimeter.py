from lc import *

# https://leetcode.com/problems/island-perimeter/discuss/95017/2-lines-in-Python

class Solution(object):
    def islandPerimeter(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);return sum([(r-1<0 or g[r-1][c]==0)+(c-1<0 or g[r][c-1]==0)+(r+1>=m or g[r+1][c]==0)+(c+1>=n or g[r][c+1]==0)for r in range(m)for c in range(n)if g[r][c]==1])

class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        return 2*sum((2-(i and g[i-1][j])-(j and r[j-1])for i,r in enumerate(g)for j,v in enumerate(r)if v))

# https://leetcode.com/problems/island-perimeter/discuss/1893713/one-line-python-convolution

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return int(abs(__import__('scipy').signal.convolve2d(grid,[[-2,1],[1,0]])).sum())

# https://leetcode.com/problems/island-perimeter/discuss/95007/Short-Python

class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        return sum(sum(map(ne,[0]+r,r+[0]))for r in g+[*map(list,zip(*g))])

class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        return sum(sum(map(ne,(0,*r),(*r,0)))for r in g+[*zip(*g)])

test('''
463. Island Perimeter
Easy

6383

341

Add to List

Share
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
Accepted
524,595
Submissions
739,761
''')
