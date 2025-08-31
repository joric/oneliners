from lc import *

# https://leetcode.com/problems/sudoku-solver/discuss/1282864/10-lines-of-Python3

class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        def f(i,j):
            for c in{*digits[1:]}-{*b[i],*[*zip(*b)][j]}-{b[i//3*3+p//3][j//3*3+p%3]for p in range(9)}:
                setitem(b[i],j,c)
                if self.solveSudoku(b):
                    return True
            setitem(b[i],j,'.')
        return next((f(i,j)for i,r in enumerate(b)for j,v in enumerate(r)if'.'==v),1)

class Solution: # TLE
    def solveSudoku(self, b: List[List[str]]) -> None:
        s,e=setitem,enumerate;return next((any(s(b[i],j,c)or self.solveSudoku(b)for c in{*digits[1:]}-{*b[i],*[*zip(*b)][j]}-{b[i//3*3+p//3][j//3*3+p%3]for p in range(9)})or s(b[i],j,'.')for i,r in e(b)for j,v in e(r)if'.'==v),1)

# https://leetcode.com/problems/sudoku-solver/submissions/1754119426/?envType=daily-question&envId=2025-08-31

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs():
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == '.':
                        for x in s9 - set(row) - {board[k][j] for k in r9} - {board[i//3*3+m][j//3*3+n] for m in r3 for n in r3}:
                            board[i][j]=x
                            if dfs():return True
                            board[i][j]='.'
                        return False
            return True
        
        r3, r9, s9 = range(3), range(9), set(map(str, range(1,10)))
        dfs()

class Solution: # 3635 ms
    def solveSudoku(self, b: List[List[str]]) -> None:
        s,e=setitem,enumerate
        def f():
            for i,r in e(b):
                for j,c in e(r):
                    if c == '.':
                        for x in {*digits[1:]}-{*r}-{b[k][j] for k in range(9)}-{b[i//3*3+p//3][j//3*3+p%3]for p in range(9)}:
                            s(b[i],j,x)
                            if f():return True
                            s(b[i],j,'.')
                        return False
            return True
        f()

class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        s,e,t,d=setitem,enumerate,range(9),{*digits[1:]}
        def f():
            for i,r in e(b):
                for j,c in e(r):
                    if c == '.':
                        return any(s(b[i],j,x)or f()or s(b[i],j,'.')for x in d-{*r}-{b[k][j] for k in t}-{b[i//3*3+p//3][j//3*3+p%3]for p in t})
            return True
        f()

# AC 1127 ms https://leetcode.com/problems/sudoku-solver/submissions/1754133913/

class Solution:
    def solveSudoku(self,b:List[List[str]])->None:
        s,e,t,d=setitem,enumerate,range(9),{*digits[1:]};(f:=lambda:next((any(s(b[i],j,x)or f()or s(b[i],j,'.')for x in d-{*r}-{b[k][j]for k in t}-{b[i//3*3+p//3][j//3*3+p%3]for p in t})for i,r in e(b)for j,c in e(r)if c=='.'),1))()

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

Other examples:

Input: board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
Output: [["7","2","1","8","5","3","9","4","6"], ["4","9","5","6","1","7","8","3","2"], ["8","3","6","4","2","9","7","5","1"], ["9","6","7","3","8","4","1","2","5"], ["2","1","4","7","6","5","3","9","8"], ["3","5","8","2","9","1","6","7","4"], ["1","7","2","5","3","6","4","8","9"], ["6","8","3","9","4","2","5","1","7"], ["5","4","9","1","7","8","2","6","3"]]


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
Accepted
555,667
Submissions
918,616
''', check=lambda res,exp,b:exp==b)