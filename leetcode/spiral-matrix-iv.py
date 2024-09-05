from lc import *

# https://leetcode.com/problems/spiral-matrix-iv/discuss/2252226/Python.-oror-10-lines-linear-algebra.-oror-TS%3A-51-97

class Solution:
    def spiralMatrix(self, m: int, n: int, h: Optional[ListNode]) -> List[List[int]]:
        a=[n*[-1]for _ in range(m)]
        def f(r,c,i,j,h):
            if h:
                if 0<=r+i<m and 0<=c+j<n and a[r+i][c+j]<0:
                    setitem(a[r+i],c+j,h.val)
                    f(r+i,c+j,i,j,h.next)
                else:
                    f(r,c,j,-i,h)
        f(0,-1,0,1,h)
        return a

class Solution:
    def spiralMatrix(self, m: int, n: int, h: Optional[ListNode]) -> List[List[int]]:
        a=[n*[-1]for _ in range(m)];(f:=lambda r,c,i,j,h:h and(0<=r+i<m and 0<=c+j<n and a[r+i][c+j]<0 and(setitem(a[r+i],c+j,h.val),f(r+i,c+j,i,j,h.next))or f(r,c,j,-i,h)))(0,-1,0,1,h);return a

test('''
2326. Spiral Matrix IV
Medium

774

27

Add to List

Share
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
Accepted
46,361
Submissions
61,084
''')
