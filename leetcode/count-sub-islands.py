from lc import *

# https://leetcode.com/problems/count-sub-islands/discuss/1284319/JavaC%2B%2BPython-DFS-Solution

class Solution:
    def countSubIslands(self, B, A):
        n, m = len(A), len(A[0])
        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and A[i][j] == 1): return 1
            A[i][j] = 0
            res = B[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res &= dfs(i + di, j + dj)
            return res
        return sum(dfs(i, j) for i in range(n) for j in range(m) if A[i][j])

class Solution:
    def countSubIslands(self, a: List[List[int]], b: List[List[int]]) -> int:
        n, m = len(b), len(b[0])
        def f(i,j):
            if  n>i>-1<j<m and b[i][j]:
                b[i][j] = 0
                r = a[i][j]
                [r:=r&x for x in map(f, (i,i+1,i-1,i),(j+1,j,j,j-1))]
                return r
            return 1
        return sum(f(i,j) for i in range(n) for j in range(m)if b[i][j])

class Solution:
    def countSubIslands(self, a: List[List[int]], b: List[List[int]]) -> int:
        n,m=len(b),len(b[0]);return sum((f:=lambda i,j:(setitem(b[i],j,0),r:=a[i][j],[r:=r&x for x in map(f, (i,i+1,i-1,i),(j+1,j,j,j-1))],r)[3]if n>i>-1<j<m and b[i][j]else 1)(i,j)for i in range(n)for j in range(m)if b[i][j])

test('''
1905. Count Sub Islands
Medium

2088

64

Add to List

Share
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
Accepted
98,199
Submissions
145,375
''')
