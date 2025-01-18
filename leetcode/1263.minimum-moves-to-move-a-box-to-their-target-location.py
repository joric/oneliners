from lc import *

# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/431528/Python-Dijkstra-Short

# TODO

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        z = lambda x,s=next,g=eq:s((i,j) for i,r in enumerate(grid) for j,c in enumerate(r) if g(c,x))
        s,b,t,f,seen = z('S'), z('B'), z('T'), z('#',set,ne), set()
        h = [(0, *s, *b)]
        while h:
            m, si, sj, bi, bj = heappop(h)
            if (bi, bj) == t:
                return m
            if (si, sj, bi, bj) in seen:
                continue
            seen.add((si, sj, bi, bj))
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                sx, sy, bx, by = si + dx, sj + dy, bi + dx, bj + dy
                if (sx, sy) == (bi, bj) and (bx, by) in f:
                    heappush(h, (m+1, sx, sy, bx, by))
                elif (sx, sy) in f and (sx, sy) != (bi, bj):
                    heappush(h, (m, sx, sy, bi, bj))
        return -1

test('''

1263. Minimum Moves to Move a Box to Their Target Location
Hard

720

50

Add to List

Share
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

Example 1:


Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.
Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1
Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.


''')
