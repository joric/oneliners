from lc import *

# https://leetcode.com/problems/minimum-cost-path-with-teleportations/solutions/7089811/python3-dp-and-prefix-min-beats-90-by-hj-lerk/

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        hi = max([max(row) for row in grid])
        dp = None
        costs = [[0] * n for _ in range(m)]
        for x in range(k + 1):
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    costs[i][j] = inf
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                    else:
                        if i < m - 1:
                            s = costs[i + 1][j] + grid[i + 1][j]
                            if s < costs[i][j]:
                                costs[i][j] = s
                        if j < n - 1:
                            s = costs[i][j + 1] + grid[i][j + 1]
                            if s < costs[i][j]:
                                costs[i][j] = s
                        if x > 0 and dp[grid[i][j]] < costs[i][j]:
                            costs[i][j] = dp[grid[i][j]]
            dp = [inf] * (hi + 1)
            for i in range(m):
                for j in range(n):
                    if costs[i][j] < dp[grid[i][j]]:
                        dp[grid[i][j]] = costs[i][j]
            dp = list(accumulate(dp,min))
        return costs[0][0]

class Solution:
    def minCost(self, g: List[List[int]], k: int) -> int:
        m,n=len(g),len(g[0])
        h=max(map(max,g))
        c=[[0]*n for _ in range(m)]
        p=None
        for x in range(k+1):
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    setitem(c[i],j,0 if i==m-1 and j==n-1 else min(inf,c[i+1][j]+g[i+1][j]if i<m-1 else inf,c[i][j+1]+g[i][j+1]if j<n-1 else inf,p[g[i][j]]if x and p[g[i][j]]<inf else inf))
            p=[inf]*(h+1);[setitem(p,g[i][j],v)for i in range(m)for j in range(n)if(v:=c[i][j])<p[g[i][j]]];p=[*accumulate(p,min)]
        return c[0][0]

class Solution:
    def minCost(self, g: List[List[int]], k: int) -> int:
        m,n,h=len(g),len(g[0]),max(map(max,g));c,p=[[0]*n for _ in range(m)],None;[([setitem(c[i],j,(i,j)!=(m-1,n-1)and+min(inf,c[i+1][j]+g[i+1][j]if i<m-1 else inf,c[i][j+1]+g[i][j+1]if j<n-1 else inf,p[g[i][j]]if x and p[g[i][j]]<inf else inf))for j in range(n-1,-1,-1)for i in range(m-1,-1,-1)],p:=[inf]*(h+1),[setitem(p,g[i][j],v)for i in range(m)for j in range(n)if(v:=c[i][j])<p[g[i][j]]],p:=[*accumulate(p,min)])for x in range(k+1)];return c[0][0]

test('''
3651. Minimum Cost Path with Teleportations
Hard
Topics
premium lock icon
Companies
Hint
You are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0) and your goal is to reach the bottom‐right cell (m - 1, n - 1).

There are two types of moves available:

Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.

Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.

Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).

 

Example 1:

Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2

Output: 7

Explanation:

Initially we are at (0, 0) and cost is 0.

Current Position    Move    New Position    Total Cost
(0, 0)  Move Down   (1, 0)  0 + 2 = 2
(1, 0)  Move Right  (1, 1)  2 + 5 = 7
(1, 1)  Teleport to (2, 2)  (2, 2)  7 + 0 = 7
The minimum cost to reach bottom-right cell is 7.

Example 2:

Input: grid = [[1,2],[2,3],[3,4]], k = 1

Output: 9

Explanation:

Initially we are at (0, 0) and cost is 0.

Current Position    Move    New Position    Total Cost
(0, 0)  Move Down   (1, 0)  0 + 2 = 2
(1, 0)  Move Right  (1, 1)  2 + 3 = 5
(1, 1)  Move Down   (2, 1)  5 + 4 = 9
The minimum cost to reach bottom-right cell is 9.

 

Constraints:

2 <= m, n <= 80
m == grid.length
n == grid[i].length
0 <= grid[i][j] <= 104
0 <= k <= 10
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,738/23.8K
Acceptance Rate
19.9%
Topics
Array
Dynamic Programming
Matrix
Biweekly Contest 163
icon
Companies
Hint 1
Use dynamic programming to solve the problem efficiently.
Hint 2
Think of the solution in terms of up to k teleportation steps. At each step, compute the minimum cost to reach each cell, either through a normal move or a teleportation from the previous step.
''')
