from lc import *

# https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return 1==max(Counter(x for i,row in enumerate(board) for j,c in enumerate(row) if c != '.' for x in ((c,i),(j,c),(i//3,j//3,c))).values()or[1])

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return len(s:=sum(([(c,i),(j,c),(i//3,j//3,c)] for i in range(9) for j in range(9) for c in [board[i][j]] if c!='.'),[]))==len(set(s))

class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        e=enumerate;return 1==max(Counter(x for i,r in e(b)for j,c in e(r)if c>'.'for x in((c,i),(j,c),(i//3,j//3,c))).values()or[1])

class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        r=range(9);return len(s:=sum(([(c,i),(j,c),(i//3,j//3,c)]for i in r for j in r for c in[b[i][j]]if c>'.'),[]))==len({*s})

test('''
36. Valid Sudoku
Medium

6918

818

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Example 3:
Input: board = [[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]]
Output: true

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
''')
