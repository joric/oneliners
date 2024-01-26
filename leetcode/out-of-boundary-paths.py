from lc import *

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * n for j in range(m)] for k in range(maxMove+1)]
        for k in range(1, maxMove+1):
            for j in range(n):
                for i in range(m):
                    dp[k][i][j] = sum(dp[k-1][x][y] if -1<x<m and -1<y<n else 1 for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)))%(10**9+7)
        return dp[maxMove][startRow][startColumn]

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(t,i,j):
            if i==m or j==n or i<0 or j<0:
                return 1
            if t==0:
                return 0
            return sum(map(dfs,[t-1]*4,(i+1,i,i-1,i),(j,j+1,j,j-1)))%(10**9+7)
        return dfs(maxMove, startRow, startColumn)

# complex numbers

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        g = {r + c*1j: 0 for r in range(m) for c in range(n)}
        @cache
        def f(t,z):
            return g.get(z,1) or t and sum(f(t-1, z + 1j**k) for k in range(4))
        return f(maxMove, startRow + startColumn*1j) % (10**9+7)

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return (g:={i+j*1j:0 for i in range(m) for j in range(n)}) and (f:=cache(lambda t,z: g.get(z,1)
            or t and sum(f(t-1,z+1j**k) for k in range(4))))(maxMove, startRow+startColumn*1j) % (10**9+7)

class Solution:
    def findPaths(self, m: int, n: int, v: int, r: int, c: int) -> int:
        g={i+j*1j:0 for i in range(m)for j in range(n)};return(f:=cache(lambda t,z:g.get(z,1)or t and sum(f(t-1,z+1j**k)for k in range(4))))(v,r+c*1j)%(10**9+7)

class Solution:
    def findPaths(self, m: int, n: int, v: int, r: int, c: int) -> int:
        g={i//n+i%n*1j:0for i in range(m*n)};return(f:=cache(lambda t,z:g.get(z,1)or t and sum(f(t-1,z+1j**k)for k in range(4))))(v,r+c*1j)%(10**9+7)

class Solution:
    def findPaths(self, m: int, n: int, v: int, r: int, c: int) -> int:
        g=set(i//n+i%n*1j for i in range(m*n));return(f:=cache(lambda t,z:g.get(z,1)or t and sum(f(t-1,z+1j**k)for k in range(4))))(v,r+c*1j)%(10**9+7)

# (shortest with the inline cache)

class Solution:
    def findPaths(self, m: int, n: int, v: int, r: int, c: int) -> int:
        return(f:=cache(lambda t,z:not(m>z.real>-1<z.imag<n)or t and sum(f(t-1,z+1j**k)for k in range(4))))(v,r+c*1j)%(10**9+7)

# https://leetcode.com/problems/out-of-boundary-paths/discuss/4628884/one-line-solution

class Solution:
    def findPaths(self, m: int, n: int, c: int, i: int, j: int) -> int:
        return (f:=cache(lambda i,j,c:not(m>i>-1<j<n) or c and sum(f(i+q,j,c-1)+f(i,j+q,c-1) for q in (-1,1))%(10**9+7)))(i,j,c)

class Solution:
    def findPaths(self, m: int, n: int, c: int, i: int, j: int) -> int:
        return(f:=cache(lambda c,i,j:not(m>i>-1<j<n)or c and sum(f(c-1,i+o,j+p)for o,p in((-1,0),(0,1),(1,0),(0,-1)))))(c,i,j)%(10**9+7)

class Solution:
    @cache
    def findPaths(self, m: int, n: int, c: int, i: int, j: int) -> int:
        return not(m>i>-1<j<n) or c and sum(self.findPaths(m,n,c-1,i+o,j+p) for o,p in ((-1,0),(0,1),(1,0),(0,-1)))%(10**9+7)

test('''

576. Out of Boundary Paths
Medium

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.


Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

''')
