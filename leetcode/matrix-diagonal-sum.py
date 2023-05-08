from lc import *

class Solution:
    def diagonalSum(self, m: List[List[int]]) -> int:
        n=len(m);return sum(m[i][i]+m[i][~i]for i in range(n))-(n%2and m[n//2][n//2])

class Solution:
    def diagonalSum(self, m: List[List[int]]) -> int:
        n=len(m);return sum(m[i][i]*(i!=~i+n)+m[i][~i]for i in range(n))

test('''
1572. Matrix Diagonal Sum
Easy

2047

27

Add to List

Share
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
Accepted
181,128
Submissions
225,244
Seen this question in a real interview before?

Yes

No
There will be overlap of elements in the primary and secondary diagonals if and only if the length of the matrix is odd, which is at the center.
''')


