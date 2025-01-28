from lc import *

# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/solutions/3696630/python-8-line-and-cpp-exchange-function/?envType=daily-question&envId=2025-01-28

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r:int, c:int) -> int:
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] < 1:
                return 0
            grid[r][c] *= -1
            return abs(grid[r][c]) + sum((dfs(r,c-1),dfs(r-1,c),dfs(r,c+1),dfs(r+1,c)))
        return max( (dfs(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c]>0), default = 0 )

class Solution:
    def findMaxFish(self, g: List[List[int]]) -> int:
        e=enumerate
        def f(i,j):
            if 0<=i<len(g) and 0<=j<len(g[0]) and g[i][j]>0:
                g[i][j] *= -1
                return abs(g[i][j]) + sum(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))
            return 0
        return max(f(i,j)for i,r in e(g)for j,x in e(r))

class Solution:
    def findMaxFish(self, g: List[List[int]]) -> int:
        e=enumerate;return+max((f:=lambda i,j:0<=i<len(g)and 0<=j<len(g[0])and(t:=g[i][j])>0 and(setitem(g[i],j,-t)or t+sum(map(f,(i+1,i,i-1,i),(j,j+1,j,j-1)))))(i,j)for i,r in e(g)for j,x in e(r))

class Solution:
    def findMaxFish(self, g: List[List[int]]) -> int:
        e=enumerate;return max(map(f:=lambda z:0<(t:=g.pop(z,0))and t+sum(f(z+1j**k)for k in range(4)),set(g:={i+j*1j:x for i,r in e(g)for j,x in e(r)})))

test('''
2658. Maximum Number of Fish in a Grid
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31.7K
Submissions
53K
Acceptance Rate
59.8%
Topics
Array
Depth-First Search
Breadth-First Search
Union Find
Matrix
Companies
Hint 1
Run DFS from each non-zero cell.
Hint 2
Each time you pick a cell to start from, add up the number of fish contained in the cells you visit.
Similar Questions
Number of Islands
Medium
Max Area of Island
Medium
''')
