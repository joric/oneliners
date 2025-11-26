from lc import *

# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/solutions/7240682/python3-using-dp-cache-by-nag007-izix/?envType=daily-question&envId=2025-11-26

class Solution:
    def numberOfPaths(self, x: List[List[int]], k: int) -> int:
        m,n = len(x), len(x[0])
        mo = (10**9) + 7
        @cache
        def f(i,j,p):
            if i>=m or j>=n:return 0
            p = (p + x[i][j])%k
            if i==m-1 and j==n-1:    
                return 1 if p==0 else 0
            return (f(i+1,j, p) + f(i,j+1, p))%mo
        ans = f(0,0,0)
        f.cache_clear()
        return ans

class Solution:
    def numberOfPaths(self, x: List[List[int]], k: int) -> int:
        m,n=len(x),len(x[0]);return+((f:=cache(lambda i,j,p:i<m and j<n and(1>(p:=(p+x[i][j])%k)and i==m-1 and j==n-1 or(f(i+1,j,p)+f(i,j+1,p))%(10**9+7))))(0,0,0),f.cache_clear())[0]

test('''
2435. Paths in Matrix Whose Sum Is Divisible by K
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
Output: 2
Explanation: There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.
Example 2:


Input: grid = [[0,0]], k = 5
Output: 1
Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.
Example 3:


Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
Output: 10
Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 5 * 104
1 <= m * n <= 5 * 104
0 <= grid[i][j] <= 100
1 <= k <= 50
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
30,845/68.7K
Acceptance Rate
44.9%
Topics
Array
Dynamic Programming
Matrix
Weekly Contest 314
icon
Companies
Hint 1
The actual numbers in grid do not matter. What matters are the remainders you get when you divide the numbers by k.
Hint 2
We can use dynamic programming to solve this problem. What can we use as states?
Hint 3
Let dp[i][j][value] represent the number of paths where the sum of the elements on the path has a remainder of value when divided by k.
Similar Questions
Unique Paths
Medium
Unique Paths II
Medium
Minimum Path Sum
Medium
Dungeon Game
Hard
Cherry Pickup
Hard
Shortest Path in Binary Matrix
Medium
Minimum Cost Homecoming of a Robot in a Grid
Medium
Check if There is a Path With Equal Number of 0's And 1's
Medium
''')
