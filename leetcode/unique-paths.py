from lc import *

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

class Solution:
    @cache
    def uniquePaths(self, m, n):
        return 1 if m==1 or n==1 else self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

class Solution:
    def uniquePaths(self, m, n):
        return(f:=cache(lambda m,n:m>1and n>1and f(m-1,n)+f(m,n-1)or 1))(m,n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2,n-1)

test('''
62. Unique Paths
Medium

14915

404

Add to List

Share
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
''')

