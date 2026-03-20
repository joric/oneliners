from lc import *

# https://leetcode.com/problems/flip-square-submatrix-vertically/solutions/7086532/python-2-line-solution-100-faster-maths-g15ya/?envType=dail

class Solution:
    def reverseSubmatrix(self, g: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x,x+k//2):
            g[i][y:y+k],g[x+k-(i-x+1)][y:y+k]=g[x+k-(i-x+1)][y:y+k],g[i][y:y+k]
        return g

# https://leetcode.com/problems/flip-square-submatrix-vertically/solutions/7470520/python-intuitive-o1-line-numpy-solution-ndxpj/?envType=daily-question&envId=2026-03-21

import numpy as np

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        matrix = np.array(grid)
        matrix[x:x+k, y:y+k] = np.flipud(matrix[x:x+k, y:y+k])
        return matrix.tolist()

class Solution:
    def reverseSubmatrix(self, g: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m=__import__('numpy').array(g);m[x:x+k,y:y+k]=m[x:x+k,y:y+k][::-1];return m.tolist()

test('''
3643. Flip Square Submatrix Vertically
Easy
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid, and three integers x, y, and k.

The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.

 

Example 1:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3

Output: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

Explanation:

The diagram above shows the grid before and after the transformation.

Example 2:

​​​​​​​
Input: grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2

Output: [[3,4,4,2],[2,3,2,3]]

Explanation:

The diagram above shows the grid before and after the transformation.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 100
0 <= x < m
0 <= y < n
1 <= k <= min(m - x, n - y)
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
64,479/88.4K
Acceptance Rate
72.9%
Topics
Mid Level
Array
Two Pointers
Matrix
Weekly Contest 462
icon
Companies
Hint 1
Use two pointers at the block's top and bottom rows and swap their k columns pairwise until the pointers meet.
''')
