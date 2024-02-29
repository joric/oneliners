from lc import *

# https://leetcode.com/problems/sudoku-solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]=='.':
                        for s in set('123456789')-set(board[i]+[board[p][j] for p in range(9)]+[board[i//3*3+p//3][j//3*3+p%3] for p in range(9)]):
                            board[i][j]=s
                            if self.solveSudoku(board): return True
                        board[i][j]='.'
                        return False
        return True

class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j]=='.':
                        for s in set(digits[1:])-set(b[i]+[b[p][j] for p in range(9)]+[b[i//3*3+p//3][j//3*3+p%3] for p in range(9)]):
                            b[i][j]=s
                            if self.solveSudoku(b): return True
                        b[i][j]='.'
                        return False
        return True

class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        return next(((lambda i,j:next((1 for s in set(digits[1:])-set(b[i]+[b[p][j]for p in range(9)]+[b[i//3*3+p//3][j//3*3+p%3]for p in range(9)])if setitem(b[i],j,s)or self.solveSudoku(b)),0)or setitem(b[i],j,'.'))(i,j)for i in range(len(b))for j in range(len(b[0]))if b[i][j]=='.'),1)

test('''
37. Sudoku Solver
Hard

9248

247

Add to List

Share
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
Accepted
555,667
Submissions
918,616
''')
