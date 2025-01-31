from lc import *

# https://leetcode.com/problems/making-a-large-island/solutions/271829/short-python-solution-with-normal-dfs-and-mark-parent/?envType=daily-question&envId=2025-01-31

class Solution(object):
    def largestIsland(self, grid):
        pa,area,lis0={},{},[]
        m,n,res=len(grid),len(grid[0]),0

        def dfs(ox,oy,x,y):
            val=1
            pa[(x,y)]=(ox,oy)

            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=i<m and 0<=j<n and grid[i][j]==1 and (i,j) not in pa:
                    val+=dfs(ox,oy,i,j)
            return val

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in pa:
                    area[(i,j)]=dfs(i,j,i,j)
                elif grid[i][j]==0:
                    lis0.append((i,j))

        for x,y in lis0:
            s=set()
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=i<m and 0<=j<n and grid[i][j]==1:
                    s.add(pa[i,j])
            res=max(res,1+sum(area[i,j] for i,j in s))

        return res if res!=0 else m*n

# TLE(!) TODO: mark islands, precalculate island areas, merge nearby islands on the 2nd pass

class Solution:
    def largestIsland(self, g: List[List[int]]) -> int:
        e=enumerate;t={i+j*1j:x for i,r in e(g)for j,x in e(r)};return max(max(map(f:=lambda z:g.pop(z,0)and 1+sum(f(z+1j**k)for k in range(4)),set(g:={z:t[z]or z==p for z in t})))for p in t)

test('''
827. Making A Large Island
Solved
Hard
Topics
Companies
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
226.1K
Submissions
454K
Acceptance Rate
49.8%
Topics
Array
Depth-First Search
Breadth-First Search
Union Find
Matrix
''')

