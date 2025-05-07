from lc import *

# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/solutions/6021695/java-dfs/?envType=daily-question&envId=2025-05-07

# TLE

class Solution:
    def minTimeToReach(self, t: List[List[int]]) -> int:
        m,n = len(t), len(t[0])
        d = [[inf] * n for _ in range(m)]
        d[0][0] = 0
        def dfs(i,j):
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0 <= x < len(t) and 0 <= y < len(t[0]):
                    if d[x][y] > d[i][j] + 1:
                        d[x][y] = max(t[x][y], d[i][j]) + 1
                        dfs(x,y)
        dfs(0,0)
        return d[m-1][n-1]

# TODO

class Solution:
    def minTimeToReach(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        dp = [[inf] * m for i in range(n)]
        h = [[0, 1, 0, 0]] # arrive time, next cost, i, j
        A[0][0] = -1
        while h:
            t, c, i, j = heappop(h)
            if t >= dp[i][j]: continue
            if i == n - 1 and j == m - 1: return t
            dp[i][j] = t
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and dp[x][y] == inf:
                    heappush(h, [max(A[x][y] + c, t + c), 2 - c, x, y])

test('''
3341. Find Minimum Time to Reach Last Room I
Solved
Medium
Topics
Companies
Hint
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
78.2K
Submissions
146.6K
Acceptance Rate
53.4%
Topics
Array
Graph
Heap (Priority Queue)
Matrix
Shortest Path
Companies
Hint 1
Use shortest path algorithms.
Similar Questions
Minimum Cost to Reach Destination in Time
Hard
Minimum Time to Visit a Cell In a Grid
Hard
''')
