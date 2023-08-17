from lc import *

# https://leetcode.com/problems/01-matrix/discuss/101102/Short-solution-Each-path-needs-at-most-one-turn

class Solution:
    def updateMatrix(self, m: List[List[int]]) -> List[List[int]]:
        a = [[10000*x for x in r] for r in m]
        for _ in range(4):
            for r in a:
                for j in range(1, len(r)):
                    r[j] = min(r[j],r[j-1]+1)
            a = [*map(list,zip(*a[::-1]))]
        return a

class Solution:
    def updateMatrix(self, m: List[List[int]]) -> List[List[int]]:
        a=[[x*10000for x in r]for r in m];[(a:=[*map(list,zip(*a[::-1]))],[setitem(r,j,min(r[j],r[j-1]+1))for r in a for j in range(1,len(r))])for _ in[0]*4];return a

class Solution:
    def updateMatrix(self, m: List[List[int]]) -> List[List[int]]:
        return reduce(lambda a,_:[*map(list,zip(*map(lambda r:accumulate(r,lambda m,x:min(m+1,x)),a[::-1])))],[0]*4,[[x*9999 for x in r]for r in m])

test('''
542. 01 Matrix
Medium

7733

348

Add to List

Share
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Example 3:
Input: mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
Output: [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
''')
