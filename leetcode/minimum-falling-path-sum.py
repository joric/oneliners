from lc import *

# https://leetcode.com/problems/minimum-falling-path-sum/solutions/1113047/python-simple-4-line-dp-solution/

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        for r in range(1, len(m)):
            for c in range(len(m[0])):
                m[r][c] += min(m[r-1][max(0,c-1):c+2])
        return min(m[-1])

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        return any(m[r].__setitem__(c,m[r][c]+min(m[r-1][max(0,c-1):c+2])) for r in range(1,len(m)) for c in range(len(m[0]))) or min(m[-1])


class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        return min(reduce(lambda f,r: [r[i]+min(f[max(i-1, 0):i+2]) for i in range(len(m))],m))

test('''

931. Minimum Falling Path Sum
Medium

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

''')
