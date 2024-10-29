from lc import *

# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/discuss/3522132/Python-3-Python-Simple-DFS-Cache-Answer

class Solution:
    def maxMoves(self, g: List[List[int]]) -> int:
        return max(map(f:=cache(lambda i,j=0:max([0]+[1+f(x,y)for x,y in((i-1,j+1),(i,j+1),(i+1,j+1))if len(g)>x>-1<y<len(g[0])and g[i][j]<g[x][y]])),range(len(g))))

test('''
2684. Maximum Number of Moves in a Grid
Medium

441

7

Add to List

Share
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

 

Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106
Accepted
25,582
Submissions
55,145
''')
