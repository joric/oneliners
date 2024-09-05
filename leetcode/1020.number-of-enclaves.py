from lc import *

# https://leetcode.com/problems/number-of-enclaves

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        h,w = len(grid),len(grid[0])
        def f(y,x):
            if h>y>=0<=x<w and grid[y][x]==1:
                grid[y][x] = 0
                any(map(f,(y-1,y,y+1,y),(x,x-1,x,x+1)))
        all((f(0,x),f(h-1,x)) for x in range(w))
        all((f(y,0),f(y,w-1)) for y in range(h))
        return sum(map(sum,grid))

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        g = {i+j*1j:x for i,r in enumerate(grid) for j,x in enumerate(r)}
        f = lambda z:g.pop(z,0) and [f(z+1j**k) for k in range(4)]!=0
        sum(f(z) for z in set(g) if not(0<z.real<len(grid)-1 and 0<z.imag<len(grid[0])-1))
        return sum(g.values())

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        return (g:={i+j*1j:x for i,r in enumerate(grid) for j,x in enumerate(r)},f:=lambda z:g.pop(z,0) and [f(z+1j**k) for k in range(4)],[f(z) for z in set(g) if not(0<z.real<len(grid)-1 and 0<z.imag<len(grid[0])-1)]) and sum(g.values())

class Solution:
    def numEnclaves(self, g: List[List[int]]) -> int:
        e,m,n=enumerate,len(g),len(g[0])
        g=Counter({i+j*1j:x for i,r in e(g) for j,x in e(r)})
        f=lambda z:g.pop(z,0)and[f(z+1j**k)for k in range(4)]
        [f(z)for z in set(g)if not n-1>z.imag>0<z.real<m-1]
        return g.total()

class Solution:
    def numEnclaves(self, g: List[List[int]]) -> int:
        e,m,n=enumerate,len(g),len(g[0]);g=Counter({i+j*1j:x for i,r in e(g)for j,x in e(r)});f=lambda z:g.pop(z,0)and[f(z+1j**k)for k in range(4)];[f(z)for z in set(g)if not n-1>z.imag>0<z.real<m-1];return g.total()

test('''
1020. Number of Enclaves
Medium

2506

44

Add to List

Share
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
Accepted
109,229
Submissions
164,051
Seen this question in a real interview before?

Yes

No
Can you model this problem as a graph problem? Create n * m + 1 nodes where n * m nodes represents each cell of the map and one extra node to represent the exterior of the map.
In the map add edges between neighbors on land cells. And add edges between the exterior and land nodes which are in the boundary. Return as answer the number of nodes that are not reachable from the exterior node.
''')
