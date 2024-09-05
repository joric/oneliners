from lc import *

# Q2. https://leetcode.com/contest/biweekly-contest-129/
# https://leetcode.com/problems/right-triangles/

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rs = [sum(row) for row in grid]
        cs = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total += (rs[i]-1)*(cs[j]-1)
        return total

class Solution:
    def numberOfRightTriangles(self, g: List[List[int]]) -> int:
        r,c=[[sum(t)for t in v]for v in (g,zip(*g))];return sum((r[i]-1)*(c[j]-1)*g[i][j]for i in range(len(g)) for j in range(len(g[0])))

test('''
3128. Right Triangles
Medium

11

1

Add to List

Share
You are given a 2D boolean matrix grid.

Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.

Note:

A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements do not have to be next to each other.
 

Example 1:

0   1   0
0   1   1
0   1   0
0   1   0
0   1   1
0   1   0
Input: grid = [[0,1,0],[0,1,1],[0,1,0]]

Output: 2

Explanation:

There are two right triangles.

Example 2:

1   0   0   0
0   1   0   1
1   0   0   0
Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]

Output: 0

Explanation:

There are no right triangles.

Example 3:

1   0   1
1   0   0
1   0   0
1   0   1
1   0   0
1   0   0
Input: grid = [[1,0,1],[1,0,0],[1,0,0]]

Output: 2

Explanation:

There are two right triangles.

 

Constraints:

1 <= grid.length <= 1000
1 <= grid[i].length <= 1000
0 <= grid[i][j] <= 1
Accepted
10,080
Submissions
24,367'''
)