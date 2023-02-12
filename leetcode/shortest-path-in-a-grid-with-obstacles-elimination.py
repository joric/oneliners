from lc import *

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q, d = deque([(0,0)]), {(0,0):(0,0)}
        while q:
            i,j = q.popleft()
            r, o = d[(i,j)]
            for m,n in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if 0<=m<len(grid) and 0<=n<len(grid[0]) and o+grid[m][n] < d.get((m,n),(0,inf))[1]:
                        d[(m,n)] = (r+1, o+grid[m][n])
                        q.append((m,n))
            r, o = d.get((len(grid)-1,len(grid[0])-1), (0,inf))
            if o <= k:
                return r
        return -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q, v = deque([(0, 0, 0, k)]), set()
        if k >= m + n - 2:
            return m + n - 2
        while q:
            steps, x, y, k = q.popleft()
            if (x, y) == (n-1, m-1):
                return steps
            for dx, dy in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0:
                    new = (dx, dy, k - grid[dy][dx])
                    if new not in v:
                        v.add(new)
                        q.append((steps + 1,) + new)
        return -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        pq = [(0, 0, 0, 0)]
        m, n = len(grid), len(grid[0])
        seen = {(0, 0):0}
        while pq:
            steps, i, j, num = heapq.heappop(pq)
            if (i, j) == (m - 1, n - 1):
                return steps
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and ((ni, nj) not in seen or seen[(ni, nj)] > num):
                    seen[(ni, nj)] = num
                    if grid[ni][nj] == 1:
                        if num < k:
                            heapq.heappush(pq, (steps + 1, ni, nj, num + 1))
                    else:
                        heapq.heappush(pq, (steps + 1, ni, nj, num))
        return -1

from queue import PriorityQueue

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = PriorityQueue()
        q.put((0,0,0,0))
        seen = {(0, 0):0}
        while not q.empty():
            steps, i, j, num = q.get()
            if (i, j) == (m - 1, n - 1):
                return steps
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and ((ni, nj) not in seen or seen[(ni, nj)] > num):
                    seen[(ni, nj)] = num
                    if grid[ni][nj] == 1:
                        if num < k:
                            q.put((steps + 1, ni, nj, num + 1))
                    else:
                        q.put((steps + 1, ni, nj, num))
        return -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def f(i, j, k, c):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return
            if k == 0 and grid[i][j] == 1:
                return
            if grid[i][j] == 2:
                return

            if self.r == len(grid) + len(grid[0]) - 2:
                return
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                self.r = min(self.r, c)
                return

            p = grid[i][j]
            grid[i][j] = 2
            if p == 1:
                k -= 1

            f(i + 1, j, k, c+1)
            f(i, j + 1, k, c+1)
            f(i - 1, j, k, c+1)
            f(i, j - 1, k, c+1)

            grid[i][j] = p

        self.r = inf
        f(0, 0, k, 0)
        return self.r if self.r!=inf else -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        g = {i+j*1j:x for i,r in enumerate(grid) for j,x in enumerate(r)}
        n = len(grid)
        m = len(grid[0])
        @cache
        def f(z, k, c):
            x = g.get(z,-1)
            if x==-1 or (k==0 and x==1) or x==2 or self.r==m+n-2:
                return
            if z==(n-1)+(m-1)*1j:
                self.r = min(self.r, c)
                return
            g[z] = 2
            if x==1:
                k -= 1
            [f(z + 1j**i,k,c+1) for i in range(4)]
            g[z] = x
        self.r = inf
        f(0, k, 0)
        return self.r if self.r!=inf else -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return ((g:={i+j*1j:x for i,r in enumerate(grid) for j,x in enumerate(r)},n:=len(grid),m:=len(grid[0]),r:=[0]),
        setitem(r,0,inf),(f:=cache(lambda z,k,c:not((x:=g.get(z,-1))==-1 or (k==0 and x==1) or x==2 or r[0]==m+n-2)
        and not(z==(n-1)+(m-1)*1j and setitem(r,0,min(r[0],c))) and (setitem(g,z,2), (x==1 and (k:=k-1)), [f(z + 1j**i,k,c+1)
        for i in range(4)],setitem(g,z,x))))(0,k,0),r[0] if r[0]!=inf else -1)[-1]

test('''
1293. Shortest Path in a Grid with Obstacles Elimination
Hard

2875

53

Add to List

Share
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0


''')
