from lc import *

# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/discuss/3650340/python-3-one-line

class Solution:
    def countPaths(self, g: List[List[int]]) -> int:
        m,n = len(g),len(g[0])
        f = cache(lambda i,j:1+sum(f(i+x,j+y) for x,y in[(0,1),(1,0),(-1,0),(0,-1)] if n>j+y>=0<=i+x<m and g[i+x][j+y]>g[i][j]))
        return sum(f(i,j) for i in range(m) for j in range(n))%(10**9+7)

class Solution:
    def countPaths(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);f=cache(lambda i,j:1+sum(f(i+x,j+y)for x,y in[(0,1),(1,0),(-1,0),(0,-1)]if n>j+y>=0<=i+x<m and g[i+x][j+y]>g[i][j]));return sum(f(i,j)for i in range(m)for j in range(n))%(10**9+7)

class Solution:
    def countPaths(self, g: List[List[int]]) -> int:
        g = {i+j*1j:x for i,r in enumerate(g) for j,x in enumerate(r)}
        f = cache(lambda z:1+sum(f(t) for k in range(4) if (t:=z+1j**k) in g and g[z]>g[t]))
        return sum(f(z) for z in g)%(10**9+7)

class Solution:
    def countPaths(self, g: List[List[int]]) -> int:
        e=enumerate;return sum(map(f:=cache(lambda z:1+sum(f(t)for k in range(4)if g[z]>g.get(t:=z+1j**k,inf))),g:={i+j*1j:x for i,r in e(g)for j,x in e(r)}))%(10**9+7)

test('''
2328. Number of Increasing Paths in a Grid
Hard

775

16

Add to List

Share
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

 

Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
1 <= grid[i][j] <= 10^5
Accepted
18,186
Submissions
37,935
Seen this question in a real interview before?

Yes

No
How can you calculate the number of increasing paths that start from a cell (i, j)? Think about dynamic programming.
Define f(i, j) as the number of increasing paths starting from cell (i, j). Try to find how f(i, j) is related to each of f(i, j+1), f(i, j-1), f(i+1, j) and f(i-1, j).
''')
