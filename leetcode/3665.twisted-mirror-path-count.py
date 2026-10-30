from lc import *

# https://leetcode.com/problems/twisted-mirror-path-count/solutions/8589919/six-simple-lines-of-code-by-mikposp-gqmf/?envType=daily-question&envId=2026-10-31

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        @cache
        def f(i,j,q,m=len(g),n=len(g[0]),M=10**9+7):
            if i//m|j//n: return 0
            if i+j==m+n-2: return 1
            return f(i+q,j+1-q,1-q) if g[i][j] else (f(i+1,j,0)+f(i,j+1,1))%M
        return f(0,0,0)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j,q,m=len(g),n=len(g[0]):0 if i//m|j//n else 1 if i+j==m+n-2 else f(i+q,j+1-q,1-q)if g[i][j]else f(i+1,j,0)+f(i,j+1,1)))(0,0,0)%(10**9+7)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j,q,m=len(g),n=len(g[0]):not i//m|j//n and 1 if i+j==m+n-2 else f(i+q,j+1-q,1-q)if g[i][j]else f(i+1,j,0)+f(i,j+1,1)))(0,0,0)%(10**9+7)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j,q,m=len(g),n=len(g[0]):not i//m|j//n and(i+j==m+n-2 or(f(i+q,j+1-q,1-q)if g[i][j]else f(i+1,j,0)+f(i,j+1,1)))))(0,0,0)%(10**9+7)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j,q,n=len(g),m=len(g[0]):i<n and j<m and(i+j==m+n-2 or(f(i+q,j+1-q,1-q)if g[i][j]else f(i+1,j,0)+f(i,j+1,1)))))(0,0,0)%(10**9+7)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j,q,n=len(g),m=len(g[0]):i-n<0>j-m and(i+j==m+n-2 or(f(i+q,j+1-q,1-q)if g[i][j]else f(i+1,j,0)+f(i,j+1,1)))))(0,0,0)%(10**9+7)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return reduce(lambda a,w,r=0:[x*(r-d)+(r:=d+r-x*r)for d,x in zip(a,w)],g,[1]+[0]*500)[-1]%(10**9+7)

class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        return eval(bytes('敲畤散氨浡摢ॡⱪⱌ㵘㨰牛⠪ⵘ⥥⠫㩘攽堫爭堪昩牯攠爬椠८楺⡰ⱪ⥌ⱝⱧㅛ⭝せ⩝〹⤰ⵛ崱⠥〱⨪⬹⤷','u16')[2:])

test('''
3665. Twisted Mirror Path Count
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n binary grid grid where:

grid[i][j] == 0 represents an empty cell, and
grid[i][j] == 1 represents a mirror.
A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 109 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

 

Example 1:

Input: grid = [[0,1,0],[0,0,1],[1,0,0]]

Output: 5

Explanation:

Number  Full Path
1   (0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2   (0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3   (0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4   (0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5   (0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
[M] indicates the robot attempted to enter a mirror cell and instead reflected.

Example 2:

Input: grid = [[0,0],[0,0]]

Output: 2

Explanation:

Number  Full Path
1   (0, 0) → (0, 1) → (1, 1)
2   (0, 0) → (1, 0) → (1, 1)
Example 3:

Input: grid = [[0,1,1],[1,1,0]]

Output: 1

Explanation:

Number  Full Path
1   (0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 500
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
15,917/33.2K
Acceptance Rate
48.0%
Topics
Staff
Array
Dynamic Programming
Matrix
Biweekly Contest 164
icon
Companies
Hint 1
Precompute, for each cell and each move (right/down), where you actually land if there’s a mirror next—store these "jump" targets in a go[i][j][0/1] table.
Hint 2
Let dp[i][j] = number of ways to reach (i,j); set dp[0][0] = 1, then scan cells in row‑major order and for each dp[i][j] > 0 add dp[i][j] into dp[x][y] for both precomputed moves.
Hint 3
Always take additions modulo 109+7, and skip any jump target that falls outside the grid.
''')
