from lc import *

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        def check(i,j):
            if mat[i][j]==0: return 0
            for x in range(n):
                if x!=i:
                    if mat[x][j]!=0: return 0
            for y in range(m):
                if y!=j:
                    if mat[i][y]!=0: return 0
            return 1
        res = 0
        for i in range(n):
            for j in range(m):
                res += check(i,j)
        return res

# https://leetcode.com/problems/special-positions-in-a-binary-matrix/discuss/3281490/Python3-oror-zip-oror-4-Line

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res=0
        for  i in zip(*mat):
            if sum(i)==1 and sum(mat[i.index(1)])==1:res+=1
        return res

class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        return sum(sum(i)==1 and sum(m[i.index(1)])==1for i in zip(*m))

test('''
1582. Special Positions in a Binary Matrix
Easy

907

33

Add to List

Share
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
Accepted
67,524
Submissions
100,486
''')

