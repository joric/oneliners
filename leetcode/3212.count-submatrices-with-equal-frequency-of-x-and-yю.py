from lc import *

# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/solutions/5431675/javacpython-dp-by-lee215-0b31/?envType=daily-question&envId=2026-03-19

class Solution:
    def numberOfSubmatrices(self, A: List[List[str]]) -> int:
        n, m = len(A), len(A[0])
        X = [[0] * (m + 1) for i in range(n + 1)]
        Y = [[0] * (m + 1) for i in range(n + 1)]
        res = 0
        for i in range(n):
            for j in range(m):
                X[i][j] = X[i-1][j] + X[i][j-1] - X[i-1][j-1] + (A[i][j] == 'X')
                Y[i][j] = Y[i-1][j] + Y[i][j-1] - Y[i-1][j-1] + (A[i][j] == 'Y')
                if X[i][j] == Y[i][j] > 0:
                    res += 1
        return res

# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/solutions/5436967/3-lines-python3-numpy-by-stefan1096-arsm/?envType=daily-question&envId=2026-03-19

import numpy as np
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        A=np.cumsum(np.cumsum(np.where(np.array(grid)=='X',1,0),axis=1),axis=0)
        B=np.cumsum(np.cumsum(np.where(np.array(grid)=='Y',1,0),axis=1),axis=0)
        return sum(i==j and i>0 for a,b in zip(A,B) for i,j in zip(a,b))

class Solution:
    def numberOfSubmatrices(self, g: List[List[str]]) -> int:
        p=__import__('numpy');a,b=[p.cumsum(np.cumsum(p.where(p.array(g)==c,1,0),axis=1),axis=0)for c in'XY'];return sum(i==j and i>0 for a,b in zip(a,b) for i,j in zip(a,b))

# POTD 2026-03-18

class Solution:
    def numberOfSubmatrices(self, g: List[List[str]]) -> int:
        n=__import__('numpy');a,b=[n.cumsum(n.cumsum(n.array(g)==c,1),0)for c in'XY'];return int(((a==b)&(a>0)).sum())

class Solution:
    def numberOfSubmatrices(self, g: List[List[str]]) -> int:
        a,b=[(__import__('numpy').array(g)==c).cumsum(1).cumsum(0)for c in'XY'];return int((a[a==b]>0).sum())

test('''
3212. Count Submatrices With Equal Frequency of X and Y
Medium
Topics
premium lock icon
Companies
Hint
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
26,937/52.2K
Acceptance Rate
51.6%
Topics
Staff
Array
Matrix
Prefix Sum
Weekly Contest 405
icon
Companies
Hint 1
Replace ’X’ with 1, ’Y’ with -1 and ’.’ with 0.
Hint 2
You need to find how many submatrices grid[0..x][0..y] have a sum of 0 and at least one ’X’.
Hint 3
Use prefix sum to calculate submatrices sum.
Similar Questions
Maximum Equal Frequency
Hard
Count Submatrices With All Ones
Medium
''')
