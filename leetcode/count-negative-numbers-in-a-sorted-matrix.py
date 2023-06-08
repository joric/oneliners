from lc import *

class Solution:
    def countNegatives(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0])
        i,j,c = 0,n-1,0
        while i<m and j>=0:
            if g[i][j]<0:
                c += m-i
                j -= 1
            else:
                i += 1
        return c

class Solution:
    def countNegatives(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0]);i,j,c = 0,n-1,0;return next(c for _ in count() if not(i<m and j>=0 and (g[i][j]<0 and(c:=c+m-i,j:=j-1)or(i:=i+1))))

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return str(grid).count('-')

test('''
1351. Count Negative Numbers in a Sorted Matrix
Easy

3344

93

Add to List

Share
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
Accepted
249,804
Submissions
330,678
Seen this question in a real interview before?

Yes

No
Use binary search for optimization or simply brute force.
''')
