from lc import *

# https://leetcode.com/problems/surrounded-regions/solutions/692740/python-3-todays-one-liner-by-l1ne-k34u/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if (n := len(board)) and (m := len(board[0])):
            def fill(x, y):
                if 0<=x<m and 0<=y<n and board[y][x] == 'O':
                    board[y][x] = '!'
                    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)): fill(x+dx,y+dy)
            for x,y in chain(product((0, m-1), range(n)), product(range(1,m-1), (0, n-1))):
                fill(x,y)
            for x,y in product(range(m), range(n)): board[y][x] = 'XO'[board[y][x]=='!']

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not any(board): return
        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]

class Solution:
    def solve(self, b: List[List[str]]) -> None:
        n,m,p=len(b),len(b[0]),product;f=lambda x,y:n>y>-1<x<m and b[y][x]=='O'and(setitem(b[y],x,'!'),[*map(f,(x-1,x+1,x,x),(y,y,y-1,y+1))]);[*map(f,*(zip(*chain(p((0,m-1),range(n)),p(range(1,m-1),(0,n-1))))))];b[:]=[['XO'[c=='!']for c in r]for r in b]

test('''
130. Surrounded Regions
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,140,328/2.6M
Acceptance Rate
44.7%
Topics
Array
Depth-First Search
Breadth-First Search
Union-Find
Matrix
icon
Companies
Similar Questions
Number of Islands
Medium
Walls and Gates
Medium
''', inplace=True)
