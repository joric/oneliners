from lc import *

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n,v,q = len(board),{1:0},[1]
        def f(j):
            x = (j - 1)%n
            y = (j - 1)//n
            c = board[~y][~x if y%2 else x]
            return c if c>0 else i
        for i in q:
            for j in range(i+1, i+7):
                k = f(j)
                if k==n*n:
                    return v[i]+1
                if k not in v:
                    v[k] = v[i]+1
                    q.append(k)
        return -1


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return (n:=len(board),v:={1:0},q:=[1]) and next((v[i]+1 for i in q for j in range(i+1,i+7) if (k:=(x:=(j-1)%n,y:=(j-1)//n) and ((c:=board[~y][y%2 and ~x or x])>0 and c or j))==n*n or (k not in v and (v.update({k:v[i]+1}) or q.append(k)))),-1)

# POTD 2025-05-31

class Solution:
    def snakesAndLadders(self, b: List[List[int]]) -> int:
        n,v,q=len(b),{1:0},[1];return next((1+v[i]for i in q for j in range(i+1,i+7)if n*n==(k:=(x:=~-j%n,y:=~-j//n)and(0<(c:=b[~y][y%2 and~x or x])and c or j))or(k not in v and(v.update({k:v[i]+1})or q.append(k)))),-1)

test('''
909. Snakes and Ladders
Medium

1149

307

Add to List

Share
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
 

Example 3:

Input: board = [[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]]
Output: 4

Constraints:

n == board.length == board[i].length
2 <= n <= 20
grid[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.

''')

