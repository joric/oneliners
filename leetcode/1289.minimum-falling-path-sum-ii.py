from lc import *

# https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/451273/Python-DP-O(MN)

class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        r = [(0, -1)]
        for t in g:
            r = nsmallest(2,((a+r[i==r[0][1]][0],i)for i,a in enumerate(t)))
        return r[0][0]

class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        return reduce(lambda s,r:sorted(((a+s[i==s[0][1]][0],i)for i,a in enumerate(r)))[:2],g,[(0,-1)])[0][0]

# https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/2905727/(Python)-simple-3-line-DP

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += min(grid[i-1][:j]+grid[i-1][j+1:])
        return min(grid[-1])

class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        [setitem(g[i],j,g[i][j]+min(g[i-1][:j]+g[i-1][j+1:]))for i in range(1,len(g))for j in range(len(g[i]))];return min(g[-1])

# https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/4509723/python-recursive-dp

class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j:g[i:]and min(f(i+1,k)+g[i][k]for k in range(len(g))if k!=j)or 0))(0,-1)

class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        return(f:=cache(lambda i,j:g[i:]and min(x+f(i+1,k)for k,x in enumerate(g[i])if k-j)or 0))(0,-1)

test('''
1289. Minimum Falling Path Sum II
Hard

1844

105

Add to List

Share
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:

Input: grid = [[7]]
Output: 7
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
Accepted
72,319
Submissions
119,590
''')