from lc import *

# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/solutions/6797785/short-and-sweet-union-find-by-tleibert-it43/?envType=daily-question&envId=2026-04-27

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        uf = list(range(m * n))
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            uf[find(x)] = find(y)
        for i, row in enumerate(grid):
            for j, street in enumerate(row):
                idx = i * n + j
                if street in (1,4,6) and j < n - 1 and grid[i][j+1] in (1,3,5):
                    union(idx + 1, idx)
                if street in (2,3,4) and i < m - 1 and grid[i+1][j] in (2,5,6):
                    union(idx + n, idx)
        return find(0) == find(m * n - 1)

# unicode find

class Solution:
    def hasValidPath(self, g: List[List[int]]) -> bool:
        e=enumerate;m,n=len(g),len(g[0]);t=''.join(map(chr,range(m*n)))
        for i,r in e(g):
            for j,v in e(r):
                k=i*n+j
                if v in(1,4,6)and j<n-1 and r[j+1]in(1,3,5):t=t.replace(t[k],t[k+1])
                if v in(2,3,4)and i<m-1 and g[i+1][j]in(2,5,6):t=t.replace(t[k],t[k+n])
        return t[0]==t[-1]

class Solution: # TLE
    def hasValidPath(self, g: List[List[int]]) -> bool:
        m,n=len(g),len(g[0]);t=''.join(map(chr,range(m*n)));all([i:=k//n,j:=k%n,v:=g[i][j],t:=t.replace(t[k],t[k+(j<n-1 and v in(1,4,6)and g[i][j+1]%2)]),t:=t.replace(t[k],t[k+n*(i<m-1 and 1<v<5 and g[i+1][j]in(2,5,6))])]for k in range(m*n));return t[0]==t[-1]

class Solution:
    def hasValidPath(self, g: List[List[int]]) -> bool:
        e=enumerate;m,n=len(g),len(g[0]);t=''.join(map(chr,range(m*n)));all((k:=i*n+j,v in(1,4,6)and j<n-1 and r[j+1]in(1,3,5)and(t:=t.replace(t[k],t[k+1])),v in(2,3,4)and i<m-1 and g[i+1][j]in(2,5,6)and(t:=t.replace(t[k],t[k+n])))for i,r in e(g)for j,v in e(r));return t[0]==t[-1]

class Solution:
    def hasValidPath(self, g: List[List[int]]) -> bool:
        m,n=len(g),len(g[0]);t=''.join(map(chr,range(m*n)));all((v:=g[i:=k//n][j:=k%n],v in(1,4,6)and j<n-1and g[i][j+1]%2and(t:=t.replace(t[k],t[k+1])),v in(2,3,4)and i<m-1and g[i+1][j]in(2,5,6)and(t:=t.replace(t[k],t[k+n])))for k in range(m*n));return t[0]==t[-1]

# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/solutions/548292/python-dfs-and-bit-manipulation-14-lines-pfns/?envType=daily-question&envId=2026-04-27

class Solution:
    def hasValidPath(self, g: List[List[int]]) -> bool:
        d, m, n = [0, 56, 146, 152, 176, 26, 50], 3*len(g), 3*len(g[0])
        def get(r, c):
            return 1 & ((0 <= r < m and 0 <= c < n) and (d[g[r//3][c//3]] >> 3*(r%3)+(c%3)))
        stack,seen = [(1,1)], {(1, 1)}
        while stack:
            (r, c) = stack.pop()
            if (r, c) == (m-2, n-2):
                return True
            for r, c in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                if (r, c) not in seen and get(r, c) == 1:
                    seen.add((r, c))
                    stack.append((r, c))
        return False

class Solution(object):
    def hasValidPath(self, g: List[List[int]]) -> bool:
        d,m,n,v=[0,56,146,152,176,26,50],3*len(g),3*len(g[0]),set()
        q=lambda i,j:1&(n>j>-1<i<m and(d[g[i//3][j//3]]>>3*(i%3)+(j%3)))
        f=cache(lambda i,j:(i,j)==(m-2,n-2)or v.add((i,j))or any(1==q(x,y)and(x,y)not in v and f(x,y)for x,y in((i-1,j),(i+1,j),(i,j+1),(i,j-1))))
        return f(1,1)

class Solution(object):
    def hasValidPath(self, g: List[List[int]]) -> bool:
        d,m,n,v=[0,56,146,152,176,26,50],3*len(g),3*len(g[0]),set();q=lambda i,j:1&(n>j>-1<i<m and(d[g[i//3][j//3]]>>3*(i%3)+(j%3)));f=cache(lambda i,j:(i,j)==(m-2,n-2)or v.add((i,j))or any(1==q(x,y)and(x,y)not in v and f(x,y)for x,y in((i-1,j),(i+1,j),(i,j+1),(i,j-1))));return f(1,1)

class Solution:
    def hasValidPath(self, g: List[List[int]]) -> bool:
        m,n,d=3*len(g),3*len(g[0]),(0,56,146,152,176,26,50);v={(1,1)};q=[*v];[(v.add((r,c)),q.append((r,c)))for i,j in q for r,c in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if m>r>-1<c<n and d[g[r//3][c//3]]>>r%3*3+c%3&1and{(r,c)}-v];return(m-2,n-2)in v

test('''
1391. Check if There is a Valid Path in a Grid
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
38,109/75.7K
Acceptance Rate
50.3%
Topics
Staff
Array
Depth-First Search
Breadth-First Search
Union-Find
Matrix
Weekly Contest 181
icon
Companies
Hint 1
Start DFS from the node (0, 0) and follow the path till you stop.
Hint 2
When you reach a cell and cannot move anymore check that this cell is (m - 1, n - 1) or not.
Similar Questions
Check if There Is a Valid Parentheses String Path
Hard
''')
