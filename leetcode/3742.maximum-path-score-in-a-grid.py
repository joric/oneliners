from lc import *

# https://leetcode.com/problems/maximum-path-score-in-a-grid/solutions/7338103/python-short-3d-dp-by-ante-p5cf/?envType=daily-question&envId=2026-04-30

class Solution:
    def maxPathScore(self, g: List[List[int]], k: int) -> int:
        n,m=len(g),len(g[0])
        @cache
        def f(i,j,c):
            if i >= n or j >= m:
                return -inf
            if (t:=c+(g[i][j]>0))>k:
                return -inf
            if i == n - 1 and j == m - 1:
                return g[i][j]
            return g[i][j] + max(f(i+1,j,t),f(i,j+1,t))
        return(max(-1,f(0,0,0)),f.cache_clear())[0]

class Solution:
    def maxPathScore(self, g: List[List[int]], k: int) -> int:
        f=cache(lambda i,j,c,n=len(g),m=len(g[0]):v+(i+j<n+m-2and max(f(i+1,j,t),f(i,j+1,t)))if i-n<0>j-m and(t:=c+(0<(v:=g[i][j])))<=k else-inf);return max(f(0,0,0),f.cache_clear()or-1)

test('''
3742. Maximum Path Score in a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1. ​​​​​​​
Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.

 

Example 1:

Input: grid = [[0, 1],[2, 0]], k = 1

Output: 2

Explanation:​​​​​​​

The optimal path is:

Cell    grid[i][j]  Score   Total
Score   Cost    Total
Cost
(0, 0)  0   0   0   0   0
(1, 0)  2   2   2   1   1
(1, 1)  0   0   2   0   1
Thus, the maximum possible score is 2.

Example 2:

Input: grid = [[0, 1],[1, 2]], k = 1

Output: -1

Explanation:

There is no path that reaches cell (1, 1)​​​​​​​ without exceeding cost k. Thus, the answer is -1.

 

Constraints:

1 <= m, n <= 200
0 <= k <= 103​​​​​​​
​​​​​​​grid[0][0] == 0
0 <= grid[i][j] <= 2
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
19,084/51.7K
Acceptance Rate
36.9%
Topics
Staff
Array
Dynamic Programming
Matrix
Weekly Contest 475
icon
Companies
Hint 1
Use dynamic programming.
Hint 2
Let dp[i][j][c] = max score at cell (i,j) with total cost exactly c (0 <= c <= k).
Hint 3
Update dp[i][j][c] from (i-1,j) and (i,j-1) using cost = (grid[i][j] == 0 ? 0 : 1) and score = grid[i][j].
Hint 4
Answer = max(dp[m-1][n-1][c]) for c=0..k, or -1 if none.
''')
