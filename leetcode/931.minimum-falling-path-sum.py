from lc import *

# https://leetcode.com/problems/minimum-falling-path-sum/solutions/1847589/python-recursion-with-memoization/

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        h,w=len(m),len(m[0])
        @cache
        def f(x,y):
            return m[x][y]+(0 if x==h-1 else min(f(x+1,y+d)for d in(-1,0,1)))if w>y>=0<=x<h else inf
        return min(f(0,i)for i in range(w))

# https://leetcode.com/problems/minimum-falling-path-sum/solutions/1113047/python-simple-4-line-dp-solution/

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        for r in range(1, len(m)):
            for c in range(len(m[0])):
                m[r][c] += min(m[r-1][max(0,c-1):c+2])
        return min(m[-1])

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        return any(setitem(m[r],c,m[r][c]+min(m[r-1][max(0,c-1):c+2])) for r in range(1,len(m)) for c in range(len(m[0]))) or min(m[-1])

# https://leetcode.com/problems/minimum-falling-path-sum/solutions/407613/python3-in-1-line

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        return min(reduce(lambda a,b:[min(a[max(i-1,0):i+2])+b[i]for i in range(len(m))],m))

class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        return min(reduce(lambda a,b:(a:=a[:2]+a)*0+[min((a:=a[1:])[:3])+c for c in b],m))

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

Example 3:

Input: matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]
Output: -36

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

''')