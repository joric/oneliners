from lc import *

# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/solutions/6802234/brute-force-by-vokasik-2y5h/?envType=daily-question&envId=2026-03-20

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R,C = len(grid), len(grid[0])
        res = [[inf] * (C - k + 1) for _ in range(R - k + 1)]
        for sr,sc in product(range(R - k + 1), range(C - k + 1)):
            nums = sorted({grid[r][c] for r,c in product(range(sr, sr + k), range(sc, sc + k))})
            if len(nums) > 1:
                for a,b in pairwise(nums):
                    res[sr][sc] = min(res[sr][sc], abs(a - b))
            else:
                res[sr][sc] = 0
        return res

class Solution:
    def minAbsDiff(self,g:List[List[int]],k:int)->List[List[int]]:
        r=range;return[[min([v-u for u,v in pairwise(sorted({g[x][y]for x in r(i,i+k)for y in r(j,j+k)}))]or[0])for j in r(len(g[0])-k+1)]for i in r(len(g)-k+1)]

class Solution:
    def minAbsDiff(self,g:List[List[int]],k:int)->List[List[int]]:
        r=range;return[[min([*map(sub,(s:=sorted({g[x][y]for x in r(i,i+k)for y in r(j,j+k)}))[1:],s)]or[0])for j in r(len(g[0])-k+1)]for i in r(len(g)-k+1)]

class Solution:
    def minAbsDiff(self,g:List[List[int]],k:int)->List[List[int]]:
        return[[min([*map(sub,(s:=sorted({x for v in g[i:i+k]for x in v[j:j+k]}))[1:],s)]or[0])for j in range(len(g[0])-k+1)]for i in range(len(g)-k+1)]

test('''
3567. Minimum Absolute Difference in Sliding Submatrix
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
 

Example 1:

Input: grid = [[1,8],[3,-2]], k = 2

Output: [[2]]

Explanation:

There is only one possible k x k submatrix: [[1, 8], [3, -2]].
Distinct values in the submatrix are [1, 8, 3, -2].
The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].
Example 2:

Input: grid = [[3,-1]], k = 1

Output: [[0,0]]

Explanation:

Both k x k submatrix has only one distinct element.
Thus, the answer is [[0, 0]].
Example 3:

Input: grid = [[1,-2,3],[2,3,5]], k = 2

Output: [[1,2]]

Explanation:

There are two possible k × k submatrix:
Starting at (0, 0): [[1, -2], [2, 3]].
Distinct values in the submatrix are [1, -2, 2, 3].
The minimum absolute difference in the submatrix is |1 - 2| = 1.
Starting at (0, 1): [[-2, 3], [3, 5]].
Distinct values in the submatrix are [-2, 3, 5].
The minimum absolute difference in the submatrix is |3 - 5| = 2.
Thus, the answer is [[1, 2]].
 

Constraints:

1 <= m == grid.length <= 30
1 <= n == grid[i].length <= 30
-105 <= grid[i][j] <= 105
1 <= k <= min(m, n)
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
20,033/29.1K
Acceptance Rate
68.9%
Topics
Senior
Array
Sorting
Matrix
Weekly Contest 452
icon
Companies
Hint 1
Use bruteforce over the submatrices
''')
