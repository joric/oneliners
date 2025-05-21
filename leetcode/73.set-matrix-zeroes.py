from lc import *

# https://leetcode.com/problems/set-matrix-zeroes/discuss/26011/Python-O(1)-solution-12-lines-of-code

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
            d = []
            h, w = len(m), len(m[0])
            for i in range(h):
                for j in range(w):
                    if m[i][j] == 0:
                        d.append((i, j))
            while d:
                i,j = d.pop()
                for x in range(w):
                    m[i][x] = 0
                for y in range(h):
                    m[y][j] = 0

# https://leetcode.com/problems/set-matrix-zeroes/discuss/4516588/No-extra-memory-required

# https://joric.github.io/interviewbit/#programming/arrays/space-recycle/set-matrix-zeros
# Use row 0 and col 0 as storage

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        h,w = len(m),len(m[0])

        c0has0, r0has0  = False, False

        for i in range(h):
            for j in range(w):
                if m[i][j] == 0:
                    m[i][0] = 0
                    m[0][j] = 0

                    if i == 0:
                        r0has0 = True
                    if j == 0:
                        c0has0 = True

        for i in range(1, h):
            for j in range(1, w):
                if m[i][0] == 0 or m[0][j]==0:
                    m[i][j] = 0

        if c0has0:
            for i in range(h):
                m[i][0] = 0

        if r0has0:
            for j in range(w):
                m[0][j] = 0

# https://leetcode.com/problems/set-matrix-zeroes/discuss/2007668/5-short-lines-of-python

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r,c=[[0 in x for x in p]for p in (m,zip(*m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                m[i][j] *= r[i]+c[j] == 0

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r,c=[[0 in x for x in p]for p in (m,zip(*m))];[setitem(m[i],j,m[i][j]*(r[i]+c[j]==0))for i in range(len(m))for j in range(len(m[0]))]

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r,c=[[0 in x for x in p]for p in(m,zip(*m))];[setitem(m[i],j,0)for i in range(len(m))for j in range(len(m[0]))if r[i]or c[j]]


class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r,c=[[0 in x for x in p]for p in(m,zip(*m))];m[:]=[[0 if r[i]or c[j]else m[i][j]for j in range(len(m[0]))]for i in range(len(m))]

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r,c=[[0 in x for x in p]for p in(m,zip(*m))];m[:]=[[m[i][j]*((r[i]+c[j])<1)for j in range(len(m[0]))]for i in range(len(m))]

test('''
73. Set Matrix Zeroes
Medium

13765

689

Add to List

Share
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
Accepted
1,251,839
Submissions
2,298,681
''', check=lambda r,e,m:all(list(x)==list(y) for x,y in zip(m,e))
)
