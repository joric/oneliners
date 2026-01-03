from lc import *

# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/?envType=daily-question&envId=2026-01-03

class Solution:
    def numOfWays(self, n: int) -> int:
        a=b=6
        for i in range(n-1):
            a,b = a*3+b*2, a*2+b*2
        return(a+b)%(10**9+7)

class Solution:
    def numOfWays(self, n: int) -> int:
        a=b=6;[(t:=a,a:=a*3+b*2,b:=t*2+b*2)for i in range(n-1)];return(a+b)%(10**9+7)

class Solution:
    def numOfWays(self, n: int) -> int:
        a=b=6;[a:=a+(b:=2*(a+b))for _ in[0]*~-n];return(a+b)%(10**9+7)

test('''
1411. Number of Ways to Paint N × 3 Grid
Hard
Topics
premium lock icon
Companies
Hint
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
42,772/65.1K
Acceptance Rate
65.7%
Topics
Dynamic Programming
Weekly Contest 184
icon
Companies
Hint 1
We will use Dynamic programming approach. we will try all possible configuration.
Hint 2
Let dp[idx][prev1col][prev2col][prev3col] be the number of ways to color the rows of the grid from idx to n-1 keeping in mind that the previous row (idx - 1) has colors prev1col, prev2col and prev3col. Build the dp array to get the answer.
Similar Questions
Painting a Grid With Three Different Colors
Hard
''')
