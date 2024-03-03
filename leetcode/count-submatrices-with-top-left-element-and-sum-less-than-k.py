from lc import *

# Q2 https://leetcode.com/contest/weekly-contest-387/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution:
    def countSubmatrices(self, g: List[List[int]], k: int) -> int:
        f=cache(lambda i,j:i>-1<j and g[i][j]+f(i-1,j)+f(i,j-1)-f(i-1,j-1));return sum(f(i,j)<=k for i,r in enumerate(g)for j in range(len(r)))

test('''
3070. Count Submatrices with Top-Left Element and Sum Less Than k
User Accepted:10344
User Tried:12269
Total Accepted:10767
Total Submissions:20161
Difficulty:Medium
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

 

Example 1:


Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
Example 2:


Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= n, m <= 1000
0 <= grid[i][j] <= 1000
1 <= k <= 109
''')
