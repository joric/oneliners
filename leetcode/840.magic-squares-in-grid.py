from lc import *

# https://leetcode.com/problems/magic-squares-in-grid/discuss/569678/Python-3-one-line

class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        return sum({g[y+dy][x+dx] for dx,dy in [(dx,dy) for dy in (-1,0,1) for dx in (-1,0,1)]}=={*range(1,10)}
            and all(sum(g[y+dy][x+dx] for dx,dy in dirs) == 15 for dirs in [*([(i,j) for i in (-1,0,1)] for j in (-1,1)),*([(j,i) for i in (-1,0,1)] for j in (-1,1)),[(i,i) for i in (-1,0,1)]])
            for y in range(1, len(g)-1) for x in range(1,len(g[0])-1))

# https://leetcode.com/problems/magic-squares-in-grid/discuss/133874/Python-5-and-43816729

class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        def isMagic(i, j):
            s = "".join(str(g[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)

# 2025-12-30 POTD

class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        return sum(g[i][j]%2<1 and''.join(str(g[i+x//3][j+x%3])for x in(0,1,2,5,8,7,6,3))in'43816729'*2+2*'92761834'for i in range(len(g)-2)for j in range(len(g[0])-2)if g[i+1][j+1]==5)

# Genmini 3 Pro

class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        return sum(r[j+1]==5>q[j]%2+4 and''.join(map(str,q[j:j+3]+[r[j+2]]+s[j:j+3][::-1]+[r[j]]))in(t:='43816729'*2)+t[::-1]for q,r,s in zip(g,g[1:],g[2:])for j in range(len(q)-2))

class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        return sum(r[j+1]==5>q[j]%2+4!=''.join(map(str,q[j:j+3]+[r[j+2]]+s[j:j+3][::-1]+[r[j]]))in'43816729'*2+2*'92761834'for q,r,s in zip(g,g[1:],g[2:])for j in range(len(q)-2))

class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:
        return sum(r[j+1]==5>q[j]%2+4!=''.join(map(str,q[j:j+3]+[r[j+2]]+s[j:j+3][::-1]+[r[j]]))in(t:='43816729'*2)+t[::-1]for q,r,s in zip(g,g[1:],g[2:])for j in range(len(q)-2))

test('''
840. Magic Squares In Grid
Medium

337

1598

Add to List

Share
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Other examples:

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2],[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 2

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
Accepted
39,787
Submissions
101,433
''')