from lc import *

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0])
        @cache
        def f(i,j):
            if not (n>j>=0<=i<m and not g[i][j]):
                return 0
            return 1 if i==m-1 and j==n-1 else f(i+1,j)+f(i,j+1)
        return f(0,0)

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);return(f:=cache(lambda i,j:int(n>j>=0<=i<m and 0==g[i][j]and(i+j==m+n-2or f(i,j+1)+f(i+1,j)))))(0,0)

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);return(f:=cache(lambda i,j:~~(n>j>=0<=i<m and 0==g[i][j]and(i+j==m+n-2or f(i,j+1)+f(i+1,j)))))(0,0)

test('''
63. Unique Paths II
Medium

7456

452

Add to List

Share
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Example 3:
Input: obstagleGrid = [[0,0],[0,1]]
Output: 0

Example 4:
Input: obstagleGrid = [[0]]
Output: 1

Example 5:
Input: obstagleGrid = [[1]]
Output: 0


Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
''')

