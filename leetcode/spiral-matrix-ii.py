from lc import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            m[i][j] = k + 1
            if m[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return m

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def f(a,b):
            m, i, j, di, dj = a
            m[i][j] = b + 1
            di, dj = (dj, -di) if m[(i+di)%n][(j+dj)%n] else (di, dj)
            i += di
            j += dj
            a = m, i, j, di, dj
            return a
        return reduce(f, range(n*n), [[[0] * n for _ in range(n)], 0, 0, 0, 1])[0]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def f(a,b):
            m, i, j, di, dj = a
            return [[m[h] if i!=h else m[h][:j]+[b+1]+m[h][j+1:] for h in range(len(m))]] + ([i+dj, j+-di, dj, -di] if m[(i+di)%n][(j+dj)%n] else [i+di, j+dj, di, dj])
        return reduce(f, range(n*n), [[[0] * n for _ in range(n)], 0, 0, 0, 1])[0]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return reduce(lambda a,b:[[a[0][h]if a[1]!=h else a[0][h][:a[2]]+[b+1]+a[0][h][a[2]+1:]for h in range(len(a[0]))]]+([a[1]+a[4],a[2]+-a[3],a[4],-a[3]]if a[0][(a[1]+a[3])%n][(a[2]+a[4])%n]else[a[1]+a[3],a[2]+a[4],a[3],a[4]]),range(n*n),[[[0]*n for _ in range(n)],0,0,0,1])[0]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m, l = [], n*n+1
        while l > 1:
            l, r = l - len(m), l
            m = [list(range(l, r))] + list(map(list,zip(*m[::-1])))
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
        return [[4*(n-(a:=min(min(i,n-i-1),min(j,n-j-1))))*a + (i>j and (4*(n-2*a-1)-(i+j-2*a)+1) or (i+j-2*a+1)) for j in range(n)] for i in range(n)]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return [[(a:=min(min(i,n-i-1),min(j,n-j-1)))*a*4*(n-a)+(i>j and 4*n-6*a-i-j-3 or i+j-2*a+1) for j in range(n)] for i in range(n)]

# https://leetcode.com/problems/spiral-matrix-ii/discuss/22391/Python-Recursive-Solution.3-lines./1348411

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return (f:=lambda l,w,b:l*[[]]and[[*range(b,b+l)]]+[*zip(*f(w-1,l,b+l)[::-1])])(n,n,1)

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