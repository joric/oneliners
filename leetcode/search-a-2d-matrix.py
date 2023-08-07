from lc import *

# https://leetcode.com/problems/search-a-2d-matrix/discuss/896821/Python-Simple-binary-search-explained

class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:
        w = len(a[0])
        l,r = 0,w*len(a)-1
        while l<r:
            m = (l+r)//2
            if a[m//w][m%w]<t:
                l = m + 1
            else:
                r = m
        return a[l//w][l%w]==t

class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:
        l,r=0,(w:=len(a[0]))*len(a)-1;return next(a[l//w][l%w]==t for _ in count() if not(l<r and (m:=(l+r)//2,a[m//w][m%w]<t and (l:=m+1)or(r:=m))))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = [row[0] for row in matrix if row]
        if not col:
            return False
        i = bisect(col, target)
        if i - 1 < 0:
            return False
        j = bisect_left(matrix[i-1], target)
        return j < len(matrix[0]) and matrix[i-1][j] == target

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        i=bisect_right([r[0]for r in m],t);j=bisect_left(m[i-1],t);return j<len(m[0])and m[i-1][j]==t

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        return t in (x for r in m for x in r)

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        return t in chain(*m)

test('''
74. Search a 2D Matrix
Medium

13263

366

Add to List

Share
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
''')
