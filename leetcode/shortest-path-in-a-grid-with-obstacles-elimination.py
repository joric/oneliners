from lc import *

class Solution1:
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

class Solution2:
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

class Solution3:
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
