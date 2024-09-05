from lc import *

# https://leetcode.com/problems/largest-local-values-in-a-matrix/discuss/4090207/One-line-solution

class Solution:
    def largestLocal(self, g: List[List[int]]) -> List[List[int]]:
        r=range(len(g)-2);return[[max(g[x][y]for x,y in product(range(i,i+3),range(j,j+3)))for j in r]for i in r]

# https://leetcode.com/problems/largest-local-values-in-a-matrix/discuss/2907214/SciPy-solution

import scipy.ndimage as nd

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        filtered = nd.maximum_filter(grid, size=(3,3))
        return filtered[1: len(grid) - 1, 1: len(grid[0]) - 1].tolist()

class Solution:
    def largestLocal(self, g: List[List[int]]) -> List[List[int]]:
        return __import__('scipy').ndimage.maximum_filter(g,size=(3,3))[1:len(g)-1,1:len(g[0])-1]

# https://leetcode.com/problems/largest-local-values-in-a-matrix/discuss/2475476/One-liner

class Solution:
    def largestLocal(self, g: List[List[int]]) -> List[List[int]]:
        t=range(len(g)-2);return[[max(max(r[c:c+3])for r in g[r:r+3])for c in t]for r in t]

test('''
2373. Largest Local Values in a Matrix
Easy

713

90

Add to List

Share
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

 

Example 1:


Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:


Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
 

Constraints:

n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100
Accepted
52,098
Submissions
62,668
''')