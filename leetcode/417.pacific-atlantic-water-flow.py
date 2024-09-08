from lc import *

class Solution:
    def pacificAtlantic(self, m: List[List[int]]) -> List[List[int]]:
        h,w,p,a = len(m), len(m[0]) if m else 0, set(), set()
        def dfs(y, x, s, v=-inf):
            if 0<=x<w and 0<=y<h and (y,x) not in s and m[y][x]>=v:
                s.add((y,x))
                list(map(dfs,(y,y,y-1,y+1),(x-1,x+1,x,x),[s]*4,[m[y][x]]*4))
        [list(map(dfs,(0,h-1),(x,x),(p,a))) for x in range(w)]
        [list(map(dfs,(y,y),(0,w-1),(p,a))) for y in range(h)]
        return p&a

class Solution:
    def pacificAtlantic(self, m: List[List[int]]) -> List[List[int]]:
        return (h:=len(m),w:=len(m[0]) if m else 0,p:=set(),a:=set(),f:=lambda y,x,s,v=-inf: 0<=x<w and 0<=y<h
            and (y,x) not in s and m[y][x]>=v and (s.add((y,x)),list(map(f,(y,y,y-1,y+1),(x-1,x+1,x,x),[s]*4,[m[y][x]]*4))),
            [list(map(f,(0,h-1),(x,x),(p,a))) for x in range(w)],[list(map(f,(y,y),(0,w-1),(p,a))) for y in range(h)],p&a)[-1]


test('''

417. Pacific Atlantic Water Flow
Medium

5743

1085

Add to List

Share
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5

''', sort=True)
