from lc import *

# https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, heap, visited, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        for i in range(n*n):
            val, x, y = heappop(heap)
            res = max(res, val)
            if x == n-1 and y == n-1:
                return res
            neib_list = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in neib_list:
                if (x + dx, y + dy) not in visited and 0<=x+dx<n and 0<=y+dy<n:
                    heappush(heap, (grid[x+dx][y+dy], x+dx, y+dy))
                    visited.add((x+dx, y+dy))

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = [[(i, j) for j in range(n)] for i in range(m)]
        def find(i, j):
            if not (i,j) == uf[i][j]:
                uf[i][j] = find(*uf[i][j])
            return uf[i][j]
        order = sorted((grid[i][j], i, j) for j in range(n) for i in range(m))
        for val, i, j in order:
            for ni, nj in [[i+1, j], [i-1,j], [i, j+1], [i, j-1]]:
                if (0<=ni<m) and (0<=nj<n) and grid[ni][nj] <= val:
                    ai, aj = find(i, j)
                    bi, bj = find(ni, nj)
                    uf[ai][aj] = uf[bi][bj]
            if find(0,0) == find(m-1, n-1):
                return val

# https://leetcode.com/problems/swim-in-rising-water/solutions/1284843/python-2-solutions-union-find-heap-explained/

class DSU(object):
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution:
    def swimInWater(self, grid):
        d, n = {}, len(grid)
        for i,j in product(range(n), range(n)):
            d[grid[i][j]] = (i, j)
        dsu = DSU(n*n)
        grid = [[0] * n for _ in range(n)] 
        neib_list = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(n*n):
            x, y = d[i]
            grid[x][y] = 1
            for dx, dy in neib_list:
                if n>x+dx>=0 and n>y+dy>=0 and grid[x+dx][y+dy] == 1:
                    dsu.union((x+dx)*n + y + dy, x*n + y)
            if dsu.find(0) == dsu.find(n*n-1):
                return i

# unicode find

class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        n = len(g)
        t,r = ''.join(map(chr,range(n*n))),range(n)
        for w,i,j in sorted((g[i][j],i,j)for i,j in product(r,r)):
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if n>y>-1<x<n and g[x][y]<w:
                    t = t.replace(t[i*n+j],t[x*n+y])
            if t[0]==t[-1]:
                return w
        return 0

class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        n=len(g);t,r=''.join(map(chr,range(n*n))),range(n);return next((w for w,i,j in sorted((g[i][j],i,j)for i,j in product(r,r))if[t:=t.replace(t[i*n+j],t[x*n+y])for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if n>y>-1<x<n and g[x][y]<w]and t[0]==t[-1]),0)

test('''
778. Swim in Rising Water
Hard

3480

231

Add to List

Share
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Example 3:

Input: grid = [[0]]
Output: 0

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n^2
Each value grid[i][j] is unique.
Accepted
145,018
Submissions
239,972
''')
