from lc import *

# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/solutions/6427839/python-dp/?envType=daily-question&envId=2025-08-27

class Solution:
    def lenOfVDiagonal(self, g: List[List[int]]) -> int:
        @cache
        def dp(i,j,x,d,k):
            if not (0 <= i < n and 0 <= j < m): return 0
            if g[i][j] != x: return 0
            res = dp(i + ds[d][0], j + ds[d][1], nx[x], d, k) + 1
            if k > 0:
                d2 = (d + 1) % 4
                res2 = dp(i + ds[d2][0], j + ds[d2][1], nx[x], d2, 0) + 1
                res = max(res, res2)
            return res

        ds = [[1,1],[1,-1],[-1,-1],[-1,1]]
        nx = [2,2,0]
        res = 0
        n, m = len(g), len(g[0])
        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    cur = max(dp(i, j, 1, d, 1) for d in range(4))
                    res = max(res, cur)
        return res

# TODO
class Solution:
    def lenOfVDiagonal(self,g:List[List[int]])->int:
        s,p,r,n,m=[[1,1],[1,-1],[-1,-1],[-1,1]],[2,2,0],0,len(g),len(g[0])
        @cache
        def f(i,j,x,d,k):
            if not(0<=i<n and 0<=j<m)or g[i][j]!=x:
                return 0
            r=f(i+s[d][0],j+s[d][1],p[x],d,k)+1
            if k:
                r=max(r,f(i+s[(d+1)%4][0],j+s[(d+1)%4][1],p[x],(d+1)%4,0)+1)
            return r
        for i in range(n):
            for j in range(m):
                if g[i][j]==1:
                    r=max(r,max(f(i,j,1,d,1)for d in range(4)))
        return r

test('''
3459. Length of Longest V-Shaped Diagonal Segment
Attempted
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
Continues the sequence in the same diagonal direction.
Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

 

Example 1:

Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:

Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 4

Explanation:



The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:

Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:

Input: grid = [[1]]

Output: 1

Explanation:

The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

 

Constraints:

n == grid.length
m == grid[i].length
1 <= n, m <= 500
grid[i][j] is either 0, 1 or 2.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
7,240/20.9K
Acceptance Rate
34.6%
Topics
Array
Dynamic Programming
Memoization
Matrix
Weekly Contest 437
icon
Companies
Hint 1
Use dynamic programming to determine the best point to make a 90-degree rotation in the diagonal path while maintaining the required sequence.
Hint 2
Represent dynamic programming states as (row, col, currentDirection, hasMadeTurnYet). Track the current position, direction of traversal, and whether a turn has already been made, and take transitions accordingly to find the longest V-shaped diagonal segment.
''')
