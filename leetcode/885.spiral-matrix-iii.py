from lc import *

# https://leetcode.com/problems/spiral-matrix-iii/discuss/158971/Python-Sort-All-Coordinates

class Solution:
    def spiralMatrixIII(self, a: int, b: int, r: int, c: int) -> List[List[int]]:
        return sorted([(i,j)for i in range(a)for j in range(b)],key=lambda p:(lambda x,y:(max(abs(x-r),abs(y-c)),-((atan2(-1,1)-atan2(x-r,y-c))%(pi*2))))(*p))

# https://leetcode.com/problems/spiral-matrix-iii/discuss/483264/Sort-coordinates-Python

class Solution:
    def spiralMatrixIII(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        return sorted([(i,j)for i in range(m)for j in range(n)],key=lambda p:(lambda i,j:(max(abs(i-r),abs(j-c)),((1,-i,j),(0,i,-j))[i+j>r+c]))(*p))

test('''
885. Spiral Matrix III
Medium

941

866

Add to List

Share
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.


Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
Accepted
51,118
Submissions
68,372
''')