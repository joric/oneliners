from lc import *

# https://leetcode.com/problems/matrix-block-sum/discuss/477516/Python3-5-line-use-defaultdict-to-avoid-out-of-index-O(m*n)

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n, S = len(mat), len(mat[0]), collections.defaultdict(int)
        for i in range(1, m + K + 1):
            for j in range(1, n + K + 1):
                S[(i, j)] = S[(i - 1, j)] + S[(i, j - 1)] - S[(i - 1, j - 1)] + (mat[i - 1][j - 1] if i - 1 < m and j - 1 < n else 0) 
        return [[S[(i + 1 + K, j + 1 + K)] - S[(i - K, j + 1 + K)] - S[(i + 1 + K, j - K)] + S[(i - K, j - K)] for j in range(n)] for i in range(m)]

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        return (m:=len(mat),n:=len(mat[0]),c:=Counter(),any(setitem(c,(i,j),c[(i-1,j)]+c[(i,j-1)]-c[(i-1,j-1)]+(mat[i-1][j-1] if i-1<m and j-1<n else 0)) for i in range(1,m+k+1) for j in range(1,n+k+1))) and [[c[(i+1+k,j+1+k)]-c[(i-k, j+1+k)]-c[(i+1+k,j-k)]+c[(i-k, j-k)] for j in range(n)] for i in range(m)]

# https://leetcode.com/problems/matrix-block-sum/discuss/1013978/Python-Super-Simple-Soln.-of-6-Lines

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n,s = len(mat),len(mat[0]),[]
        for i in range(m):
            c = list(map(sum,(zip(*mat[max(i-k,0):min(i+k+1,m)]))))
            s.append([sum(c[max(j-k, 0): min(j+k+1, n)]) for j in range(n)])
        return s

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        return (m:=len(mat),n:=len(mat[0])) and [[sum([*map(sum,(zip(*mat[max(i-k,0):min(i+k+1,m)])))][max(j-k, 0):min(j+k+1,n)]) for j in range(n)] for i in range(m)]

test('''

1314. Matrix Block Sum
Medium

2138

327

Add to List

Share
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100

Accepted
75,621
Submissions
100,280

''')
