from lc import *

# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/solutions/6067031/beats-100-video-full-explain-3-approache-q1b8/?envType=daily-question&envId=2025-11-02

class Solution:
    def countUnguarded(self, m: int, n: int, g: List[List[int]], w: List[List[int]]) -> int:
        d = [[0]*n for _ in range(m)]
        for i,j in g+w:
            d[i][j] = 1
        for a,b in g:
            for i,j in [(-1,0),(0,1),(1,0),(0,-1)]:
                x,y = a,b
                while m>x+i>-1<y+j<n and d[x+i][y+j]!=1:
                    x += i
                    y += j
                    d[x][y] = 2
        return sum(v.count(0) for v in d)

class Solution:
    def countUnguarded(self, m: int, n: int, g: List[List[int]], w: List[List[int]]) -> int:
        d=[[0]*n for _ in range(m)];[setitem(d[i],j,1)for i,j in g+w];[(x:=a,y:=b,all(m>x+i>-1<y+j<n and d[x+i][y+j]!=1 and[setitem(d[x:=x+i],y:=y+j,2)]for _ in range(m*n)))for i,j in((-1,0),(0,1),(1,0),(0,-1))for a,b in g];return sum(v.count(0) for v in d)

test('''
2257. Count Unguarded Cells in the Grid
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
110,196/167.8K
Acceptance Rate
65.7%
Topics
Array
Matrix
Simulation
Biweekly Contest 77
icon
Companies
Hint 1
Create a 2D array to represent the grid. Can you mark the tiles that can be seen by a guard?
Hint 2
Iterate over the guards, and for each of the 4 directions, advance the current tile and mark the tile. When should you stop advancing?
Similar Questions
Bomb Enemy
Medium
Available Captures for Rook
Easy
''')
