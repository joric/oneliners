from lc import *

class Solution:
    def transpose(self, m: List[List[int]]) -> List[List[int]]:
        return zip(*m)

test('''
867. Transpose Matrix
Easy

3221

431

Add to List

Share
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.



 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
-109 <= matrix[i][j] <= 10^9
Accepted
290,233
Submissions
432,765
''')

