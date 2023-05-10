from lc import *

# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m,a = [],n*n+1
        while a>1:
            a,b = a-len(m),a
            m = [[*range(a,b)]]+[*zip(*m[::-1])]
        return m

# https://leetcode.com/problems/spiral-matrix-ii/discuss/1941546/Python3-1-line-solution

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return [[4*(n-min(min(i,n-i-1),min(j,n-j-1)))*min(min(i,n-i-1),min(j,n-j-1)) + ((i+j-2*min(min(i,n-i-1),min(j,n-j-1))+1) if (i <= j) else (4*(n-2*min(min(i,n-i-1),min(j,n-j-1))-1)-(i+j-2*min(min(i,n-i-1),min(j,n-j-1)))+1)) for j in range(n)] for i in range(n)]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return [[4*(n-(a:=min(min(i,n-i-1),min(j,n-j-1))))*a + ((i+j-2*a+1) if i<=j else (4*(n-2*a-1)-(i+j-2*a)+1)) for j in range(n)] for i in range(n)]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r=range(n);return[[4*(n-(a:=min(i,j,~i+n,~j+n)))*a+(i+j-2*a+1,4*n-6*a-i-j-3)[i>j]for j in r]for i in r]

# https://leetcode.com/problems/spiral-matrix-ii/discuss/22391/Python-Recursive-Solution.3-lines./1348411

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return (f:=lambda a,b,c:a*[[]]and[[*range(c,c+a)]]+[*zip(*f(b-1,a,c+a)[::-1])])(n,n,1)

test('''
59. Spiral Matrix II

Medium

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 20
''')