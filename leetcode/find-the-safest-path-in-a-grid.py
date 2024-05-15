from lc import *

# https://leetcode.com/problems/find-the-safest-path-in-a-grid/discuss/3900479/Python-3-oror-25-lines-queue-and-heap-oror-TM%3A-94-52

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q,v = deque(),[[-1]*n for _ in range(n)]
        w = set(product(range(n),range(n)))
        e = lambda x,y:set(((x-1,y),(x,y-1),(x+1,y),(x,y+1)))&w
        for i,j in product(range(n),range(n)):
            if grid[i][j] == 1:
                v[i][j] = 0
                q.append((0, i,j))
        while q:
            s, x,y = q.popleft()
            for i,j in e(x,y):
                if v[i][j] == -1:
                    v[i][j] = s + 1
                    q.append((s+1,i,j))
        h = [(-v[-1][-1],n-1,n-1)]
        while h:
            s,x,y = heappop(h)
            if (x,y)==(0,0):
                return min(-s,v[0][0])
            w.discard((x,y))
            for i,j in e(x,y):
                heappush(h,(max(s,-v[i][j]),i,j))
                w.discard((i,j))
        return -1

class Solution:
    def maximumSafenessFactor(self, g: List[List[int]]) -> int:
        n=len(g);q,v=deque(),[[-1]*n for _ in range(n)];w=set(product(range(n),range(n)));e=lambda x,y:set(((x-1,y),(x,y-1),(x+1,y),(x,y+1)))&w
        [setitem(v[i],j,0)or q.append((0,i,j))for i,j in product(range(n),range(n))if g[i][j]==1]
        while q:
            s,x,y = q.popleft()
            [setitem(v[i],j,s+1)or q.append((s+1,i,j))for i,j in e(x,y)if v[i][j]==-1]
        h=[(-v[-1][-1],n-1,n-1)]
        while h:
            s,x,y = heappop(h)
            if (x,y)==(0,0):
                return min(-s,v[0][0])
            w.discard((x,y))
            [heappush(h,(max(s,-v[i][j]),i,j))or w.discard((i,j))for i,j in e(x,y)]
        return -1

class Solution:
    def maximumSafenessFactor(self, g: List[List[int]]) -> int:
        n=len(g);q,v=deque(),[[-1]*n for _ in range(n)];w=set(product(range(n),range(n)));e=lambda x,y:set(((x-1,y),(x,y-1),(x+1,y),(x,y+1)))&w
        [setitem(v[i],j,0)or q.append((0,i,j))for i,j in product(range(n),range(n))if g[i][j]==1]
        q and(f:=lambda s,x,y:([setitem(v[i],j,s+1)or q.append((s+1,i,j))for i,j in e(x,y)if v[i][j]==-1],q and f(*q.popleft())))(*q.popleft())
        h=[(-v[-1][-1],n-1,n-1)]
        f=lambda s,x,y:min(-s,v[0][0])if(x,y)==(0,0)else(w.discard((x,y)),[heappush(h,(max(s,-v[i][j]),i,j))or w.discard((i,j))for i,j in e(x,y)])and h and f(*heappop(h))
        return f(*heappop(h))if h else -1

test('''
2812. Find the Safest Path in a Grid
Medium

793

96

Add to List

Share
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

 

Example 1:


Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
Example 2:


Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
Example 3:


Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
 

Other examples:

Input: grid = [[1,1,1],[1,1,1],[1,1,0]]
Output: 0

Constraints:

1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
Accepted
19,870
Submissions
61,917
''')
