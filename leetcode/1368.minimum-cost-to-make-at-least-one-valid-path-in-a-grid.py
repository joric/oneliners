from lc import *

# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solutions/4993584/14-line-simple/?envType=daily-question&envId=2025-01-18

from sortedcontainers import SortedList
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dist = [[inf for j in range(C)] for i in range(R)]
        dist[-1][-1] = 0
        sl = SortedList([(0, R-1, C-1)])
        seen = set()
        while sl:
            d, r, c = sl.pop(0)
            if d > dist[r][c] or (r, c) in seen: continue
            dist[r][c] = d
            seen.add((r, c))
            for dr, dc, t in [[-1, 0, 3], [1, 0, 4], [0, 1, 2], [0, -1, 1]]:
                if 0<=r+dr<R and 0<=c+dc<C: sl.add((d+(grid[r+dr][c+dc] != t), r+dr, c+dc))
        return dist[0][0]

# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solutions/524886/java-c-python-bfs-and-dfs/?envType=daily-question&envId=2025-01-18

class Solution:
    def minCost(self, A):
        n, m, inf, k = len(A), len(A[0]), 10**9, 0
        dp = [[inf] * m for i in range(n)]
        dirt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        bfs = []

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and dp[x][y] == inf): return
            dp[x][y] = k
            bfs.append([x, y])
            dfs(x + dirt[A[x][y] - 1][0], y + dirt[A[x][y] - 1][1])

        dfs(0, 0)
        while bfs:
            k += 1
            bfs, bfs2 = [], bfs
            [dfs(x + i, y + j) for x, y in bfs2 for i, j in dirt]
        return dp[-1][-1]

# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solutions/810149/python-djikstra-o-mnlog-mn-time-space/?envType=daily-question&envId=2025-01-18

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        h = [(0, 0, 0)]
        dirs = [(1, 0, 1), (2, 0, -1), (3, 1, 0), (4, -1, 0)]
        seen = set()
        valid = lambda i, j: i in range(N) and j in range(M)
        while h:
            cost, i, j = heappop(h)
            if (i, j) == (N - 1, M - 1):
                return cost
            if (i, j) in seen: continue
            seen.add((i, j))
            for n, di, dj in dirs:
                if valid(i + di, j + dj):
                    heappush(h, (int(n != grid[i][j]) + cost, i + di, j + dj))

class Solution:
    def minCost(self, g: List[List[int]]) -> int:
        n,m,h,v=len(g),len(g[0]),[(0,0,0)],set()
        r = lambda i,j:i in range(n)and j in range(m)
        while h:
            c,i,j = heappop(h)
            if (i,j) == (n-1,m-1):
                return c
            if (i,j) not in v:
                v.add((i, j))
                for d,x,y in [(1,0,1),(2,0,-1),(3,1,0),(4,-1,0)]:
                    if r(i+x,j+y):
                        heappush(h,(int(d!=g[i][j])+c,i+x,j+y))

class Solution:
    def minCost(self, g: List[List[int]]) -> int:
        n,m,h,v=len(g),len(g[0]),[(0,0,0)],set();return(f:=lambda c,i,j:c if(i,j)==(n-1,m-1)else[(i,j)not in v and(v.add((i,j)),[(lambda i,j:i in range(n)and j in range(m))(i+x,j+y)and heappush(h,(int(d!=g[i][j])+c,i+x,j+y))for d,x,y in [(1,0,1),(2,0,-1),(3,1,0),(4,-1,0)]])]and h and f(*heappop(h)))(*heappop(h))

test('''
1368. Minimum Cost to Make at Least One Valid Path in a Grid
Solved
Hard
Topics
Companies
Hint
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

 

Example 1:


Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:


Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:


Input: grid = [[1,2],[4,3]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
Seen this question in a real interview before?
1/5
Yes
No
Accepted
65.1K
Submissions
100.4K
Acceptance Rate
64.9%
''')

