from lc import *

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/5974487/One-Line-Solution

class Solution:
    def countSquares(self, g: List[List[int]]) -> int:
        return sum(starmap(f:=cache(lambda i,j:i*j*g[i][j]and 1+min(f(i,j-1),f(i-1,j-1),f(i-1,j))or g[i][j]),product(range(len(g)),range(len(g[0])))))

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))

class Solution:
    def countSquares(self, g: List[List[int]]) -> int:
        [setitem(g[i],j,g[i][j]*(min(g[i-1][j],g[i][j-1],g[i-1][j-1])+1))for i in range(1,len(g))for j in range(1,len(g[0]))];return sum(map(sum,g))

test('''
1277. Count Square Submatrices with All Ones
Medium

4910

83

Add to List

Share
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
Accepted
237,224
Submissions
313,663
''')
