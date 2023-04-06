from lc import *

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        h,w = len(grid), len(grid[0])
        def f(y,x):
            if 0<=y<h and 0<=x<w and grid[y][x]==0:
                grid[y][x] = 1
                any(map(f,(y-1,y,y+1,y),(x,x-1,x,x+1)))

        for y in range(h):
            for x in range(w):
                if y==0 or x==0 or y==h-1 or x==w-1:
                    f(y,x)
        r = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    f(y,x)
                    r += 1
        return r

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        h,w = len(grid), len(grid[0])
        def f(y,x):
            if 0<=y<h and 0<=x<w and grid[y][x]==0:
                grid[y][x] = 1
                any(map(f,(y-1,y,y+1,y),(x,x-1,x,x+1)))
        any(any(map(f,(0,h-1),(x,x))) for x in range(w))
        any(any(map(f,(y,y),(0,w-1))) for y in range(h))
        return sum(grid[y][x]==0 and not f(y,x) for y in range(h) for x in range(w))

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        return (h:=len(grid),w:=len(grid[0]),f:=lambda y,x:0<=y<h and 0<=x<w and grid[y][x]==0 and not(setitem(grid[y],x,1),any(map(f,(y-1,y,y+1,y),(x,x-1,x,x+1)))),any(any(map(f,(0,h-1),(x,x))) for x in range(w)),any(any(map(f,(y,y),(0,w-1))) for y in range(h))) and sum(grid[y][x]==0 and not f(y,x) for y in range(h) for x in range(w))

test('''
1254. Number of Closed Islands
Medium

2990

91

Add to List

Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
Accepted
135,398
Submissions
209,967
Seen this question in a real interview before?

Yes

No
Exclude connected group of 0s on the corners because they are not closed island.
Return number of connected component of 0s on the grid.
''')

