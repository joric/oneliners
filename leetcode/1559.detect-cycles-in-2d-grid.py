from lc import *

# https://leetcode.com/problems/detect-cycles-in-2d-grid/solutions/806630/python3-memoized-dfs-with-a-direction-pa-0kz0/?envType=daily-question&envId=2026-04-26

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def fn(i, j, d): 
            """Traverse the grid to find cycle via backtracking."""
            if grid[i][j] != "BLACK": 
                val = grid[i][j]
                grid[i][j] = "GRAY" # mark visited in this trial
                for ii, jj, dd in ((i-1, j, -2), (i, j-1, -1), (i, j+1, 1), (i+1, j, 2)):
                    if 0 <= ii < m and 0 <= jj < n and d + dd != 0: # in range & not going back 
                        if grid[ii][jj] == "GRAY": return True #cycle found 
                        if grid[ii][jj] == val: fn(ii, jj, dd)
                grid[i][j] = val 
        
        for i in range(m):
            for j in range(n):
                if fn(i, j, 0): return True
                grid[i][j] = "BLACK" # mark "no cycle"
        return False 

class Solution:
    def containsCycle(self,g:List[List[str]])->bool:
        m,n,s=len(g),len(g[0]),setitem;f=cache(lambda i,j,d:g[i][j]and(v:=g[i][j],s(g[i],j,1),any(1==g[x][y]or v==g[x][y]and f(x,y,c)for x,y,c in((i-1,j,-2),(i,j-1,-1),(i,j+1,1),(i+1,j,2))if n>y>-1<x<m and d+c)or s(g[i],j,v))[2]);return any(f(i,j,0)or s(g[i],j,0)for i in range(m)for j in range(n))

class Solution:
    def containsCycle(self,g:List[List[str]])->bool:
        m,n,s=len(g),len(g[0]),setitem;f=cache(lambda i,j,d:(v:=g[i][j])and(s(g[i],j,1)or any(1==g[x][y]or v==g[x][y]and f(x,y,c)for x,y,c in((i-1,j,-2),(i,j-1,-1),(i,j+1,1),(i+1,j,2))if n>y>-1<x<m and d+c)or s(g[i],j,v)));return any(f(i:=k//n,j:=k%n,0)or s(g[i],j,0)for k in range(m*n))

# https://leetcode.com/problems/detect-cycles-in-2d-grid/solutions/6662878/dfs-by-shashwatbangar-lj6q/

class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        m,n,v=len(g),len(g[0]),set()
        def f(i,j,a,b,c):
            if n>j>-1<i<m and g[i][j]==c:
                if (i,j)in v:
                    return 1
                v.add((i,j))
                return any((x!=a or y!=b)and f(x,y,i,j,c)for x,y in ((i,j+1),(i+1,j),(i-1,j),(i,j-1)))
        return any((i:=k//n,j:=k%n)not in v and f(i,j,-1,-1,g[i][j])for k in range(m*n))

class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        m,n,v=len(g),len(g[0]),set();f=lambda i,j,a,b,c:(n>j>-1<i<m and g[i][j]==c)and(v&{(i,j)}or v.add((i,j))or any((x!=a or y!=b)and f(x,y,i,j,c)for x,y in((i,j+1),(i+1,j),(i-1,j),(i,j-1))));return any(f(i,j,-1,-1,g[i][j])for k in range(m*n)if{(i:=k//n,j:=k%n)}-v)

class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        m,n,v=len(g),len(g[0]),set();f=lambda i,j,a,b,c:(n>j>-1<i<m and g[i][j]==c)and(v&{(i,j)}or v.add((i,j))or any(f(x,y,i,j,c)for x,y in((i,j+1),(i+1,j),(i-1,j),(i,j-1))if x!=a or y!=b));return any(f(i,j,-1,-1,g[i][j])for k in range(m*n)if{(i:=k//n,j:=k%n)}-v)

class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        m,n,v=len(g),len(g[0]),set();f=lambda i,j,a,b,c:(n>j>-1<i<m and g[i][j]==c)and(v&{(i,j)}or v.add((i,j))or any(f(x,y,i,j,c)for x,y in((i,j+1),(i+1,j),(i-1,j),(i,j-1))if(x,y)!=(a,b)));return any(f(i,j,-1,-1,g[i][j])for k in range(m*n)if{(i:=k//n,j:=k%n)}-v)

class Solution:
    def containsCycle(self, g: List[List[str]]) -> bool:
        v,e,f=set(),enumerate,lambda i,j,p,x:len(g)>i>-1<j<len(g[i])and x==g[i][j]and(v&{t:=(i,j)}or v.add(t)or any(f(*d,t,x)for d in((i+1,j),(i,j+1),(i-1,j),(i,j-1))if d!=p));return any(f(i,j,0,x)for i,r in e(g)for j,x in e(r)if{(i,j)}-v)

test('''
1559. Detect Cycles in 2D Grid
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid consists only of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
68,957/130.2K
Acceptance Rate
52.9%
Topics
Senior Staff
Array
Depth-First Search
Breadth-First Search
Union-Find
Matrix
Biweekly Contest 33
icon
Companies
Hint 1
Keep track of the parent (previous position) to avoid considering an invalid path.
Hint 2
Use DFS or BFS and keep track of visited cells to see if there is a cycle.
''')
