from lc import *

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.r = 0
        def f(i,j):
            if x:=grid.pop((i,j),0):
                if x==3 and not grid:
                    self.r += 1
                list(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))
                grid.update({(i,j): x})
        grid = {(i,j): x + 1 for j, row in enumerate(grid) for i, x in enumerate(row) if x!=-1}
        f(*next((i,j) for (i,j),v in grid.items() if v==2))
        return self.r

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def f(z,r):
            if x:=g.pop(z,0):
                if x==3 and not g:
                    r = r + 1
                for k in range(4):
                   r = f(z + 1j**k, r)
                g.update({z:x})
            return r
        g = {i + j*1j:x+1 for i, row in enumerate(grid) for j,x in enumerate(row) if x!=-1}
        return f(next(z for z,x in g.items() if x==2),0)

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return (g:={i + j*1j:x+1 for i, row in enumerate(grid) for j,x in enumerate(row) if x!=-1}) and (f:=lambda z,r:[(x:=g.pop(z,0)) and (x==3 and not g and (r:=r+1), [r:=f(z + 1j**k,r) for k in range(4)],g.update({z:x}))] and r)(next(z for z,x in g.items() if x==2),0)


test('''

980. Unique Paths III
Hard

3988

156

Add to List

Share
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.

''')


