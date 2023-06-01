from lc import *

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = deque([(0,0,1)])
        seen = set((0,0))
        while q:
            i,j,dist = q.popleft()
            if i == n-1 and j == n-1:
                return dist
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and (x,y) not in seen and grid[x][y] == 0:
                    seen.add((x, y))
                    q.append((x, y, dist + 1))
        return -1 

class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        n = len(g)
        q = deque([(0,0,1)])
        s = set((0,0))
        while not(g[0][0]or g[n-1][n-1]) and q:
            i,j,d = q.popleft()
            if i == n-1 and j == n-1:
                return d
            for x,y in product([i,i-1,i+1],[j,j-1,j+1]):
                if n>y>=0<=x<n and(x,y)not in s and g[x][y]==0:
                    s.add((x,y))
                    q.append((x,y,d+1))
        return -1 

class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        n,q,s=len(g),deque([(0,0,1)]),set((0,0))
        while not(g[0][0] or g[n-1][n-1]) and q:
            i,j,d = q.popleft()
            if i==n-1 and j==n-1:
                return d
            [s.add((x,y)) or q.append((x,y,d+1)) for x,y in product([i,i-1,i+1],[j,j-1,j+1]) if n>y>=0<=x<n and(x,y) not in s and g[x][y]==0]
        return -1

class Solution:
    def shortestPathBinaryMatrix(self, g):
        n = len(g) 
        d = [999]*n*n
        d[0] = 1
        a = range(n)
        b = range(-1,2)
        e = [(i*n+j,(i+k)*n+j+l) for i,j,k,l in product(a,a,b,b) if 0<=i+k<n and 0<=j+l<n and g[i][j]+g[i+k][j+l]==0]
        for _ in range(int(2*n**0.5)+2):
            for u,v in e:
                d[v] = min(d[v],d[u]+1)
        return d[-1] if g[-1][-1]!=1 and d[-1]!=999 else -1

class Solution:
    def shortestPathBinaryMatrix(self, g):
        n=len(g);d,a,b=[999]*n*n,range(n),range(-1,2);e=[(i*n+j,(i+k)*n+j+l) for i,j,k,l in product(a,a,b,b) if 0<=i+k<n and 0<=j+l<n and g[i][j]+g[i+k][j+l]==0];d[0]=1;[setitem(d,v,min(d[v],d[u]+1)) for _ in range(int(2*n**0.5)+2) for u,v in e];return g[-1][-1]!=1 and d[-1]!=999 and d[-1] or -1

test('''
1091. Shortest Path in Binary Matrix
Medium

5035

193

Add to List

Share
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
Accepted
324,033
Submissions
713,275
Seen this question in a real interview before?

Yes

No
Do a breadth first search to find the shortest path.
''')

