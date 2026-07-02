from lc import *

# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/editorial/?envType=daily-question&envId=2026-07-02

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dis = [[float("inf")] * n for _ in range(m)]
        q = deque()
        q.appendleft((0, 0))
        dis[0][0] = grid[0][0]
        while q:
            cx, cy = q.popleft()
            # the first time it leaves the queue, the shortest distance is guaranteed
            if cx == m - 1 and cy == n - 1:
                return True
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                cost = dis[cx][cy] + grid[nx][ny]
                # pruning: the new distance does not meet health requirements
                if cost >= health:
                    continue

                if cost < dis[nx][ny]:
                    dis[nx][ny] = cost
                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))
        return False


# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/solutions/8370818/12-lines-of-python-code-beats-100-32ms-o-mnnj/

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        m,n = len(g[0]), len(g)
        d = [[0]*m for _ in range(n)]
        d[0][0]=h-g[0][0]
        q = deque([(d[0][0],0,0)])
        while q:
            h,i,j=q.popleft()
            for x, y in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
                if 0 <= x < n and 0 <= y < m and (t := h - g[x][y]) > d[x][y]:
                    d[x][y] = t
                    (q.append,q.appendleft)[t==y]((t,x,y))
        return d[-1][-1] > 0

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        m,n=len(g[0]),len(g);d=[m*[0]for _ in g];d[0][0]=h-g[0][0];q=deque();f=lambda h,i,j:([setitem(d[x],y,t)or(q.append,q.appendleft)[t==y]((t,x,y))for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if m>y>-1<x<n and(t:=h-g[x][y])>d[x][y]],q and f(*q.popleft()));return f(d[0][0],0,0)and d[-1][-1]>0

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        m,n=len(g[0]),len(g);d=defaultdict(int);d[0,0]=h-g[0][0];q=deque();f=lambda c,i,j:any(setitem(d,(x,y),t)or(q.append,q.appendleft)[t==c]((t,x,y))for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if n>x>-1<y<m and(t:=c-g[x][y])>d[x,y])or q and f(*q.popleft());return f(d[0,0],0,0)or d[n-1,m-1]>0

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        q=[(g[0][0],(0,0))];v=set();m=len(g);n=len(g[0]);return any(q and((p:=q.pop(0)),(u:=p[1])not in v and(v.add(u),[q.insert(len(q)*(w:=g[r][c]),(p[0]+w,(r,c)))for x,y in((0,1),(1,0),(0,-1),(-1,0))if m>(r:=u[0]+x)>-1<(c:=u[1]+y)<n]),u==(m-1,n-1)and h>p[0])[-1]for _ in range(m*n*5))

# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/solutions/5787169/python-dfs-by-prashasst-mn44/?envType=daily-question&envId=2026-07-02

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        self.reached=False
        visited = [[False for _ in range(n)] for _ in range(m)]
        @cache
        def dfs(r,c,h):
            if r<0 or r>=m or c<0 or c>=n or visited[r][c] or h<=0 :return
            visited[r][c]=True
            if grid[r][c]==1:
                h-=1
                if h<1:
                    visited[r][c]=False
                    return 
            if r==m-1 and c==n-1:
                if h>0:
                    self.reached=True
                visited[r][c]=False
                return
            x = [1, -1, 0, 0]
            y = [0, 0, 1, -1]
            for xi,yi in zip(x,y):
                dfs(r+yi,c+xi,h)
            visited[r][c]=False
        dfs(0,0,health)
        return self.reached

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        q=[];v=set();m=len(g);n=len(g[0]);d=(0,1,0,-1,0)
        def f(c,r,x):
            if (r,x) not in v:
                v.add((r,x))
                if (r,x)==(m-1,n-1) and h>c:
                    return True
                [0<=(a:=r+i)<m and 0<=(b:=x+j)<n and heappush(q,(c+g[a][b],a,b))for i,j in zip(d,d[1:])]
            return q>[]and f(*heappop(q))
        return f(g[0][0],0,0)

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        q=[];v=set();m=len(g);n=len(g[0]);d=(0,1,0,-1,0);f=lambda c,r,x:((r,x)not in v and(v.add((r,x))or((r,x)==(m-1,n-1)and h>c)or([0<=(a:=r+i)<m and 0<=(b:=x+j)<n and heappush(q,(c+g[a][b],a,b)) for i,j in zip(d,d[1:])]>[]and False)))or(q>[]and f(*heappop(q)));return f(g[0][0],0,0)

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        q=[(g[0][0],(0,0))];v=set();m=len(g);n=len(g[0]);return any(q and((p:=heappop(q)),(u:=p[1])not in v and(v.add(u),[heappush(q,(p[0]+g[r][c],(r,c)))for x,y in((0,1),(1,0),(0,-1),(-1,0))if 0<=(r:=u[0]+x)<m and 0<=(c:=u[1]+y)<n]),u==(m-1,n-1)and h>p[0])[-1]for _ in range(m*n*5))

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        q=[(g[0][0],(0,0))];v=set();m=len(g);n=len(g[0]);return any(q and((p:=heappop(q)),(u:=p[1])not in v and(v.add(u),[heappush(q,(p[0]+g[r][c],(r,c)))for x,y in((0,1),(1,0),(0,-1),(-1,0))if-1<(r:=u[0]+x)<m and-1<(c:=u[1]+y)<n]),u==(m-1,n-1)and h>p[0])[-1]for _ in range(m*n*5))

class Solution:
    def findSafeWalk(self, g: List[List[int]], h: int) -> bool:
        q=[(g[0][0],(0,0))];v=set();m=len(g);n=len(g[0]);return any(q and((p:=heappop(q)),(u:=p[1])not in v and(v.add(u),[heappush(q,(p[0]+g[r][c],(r,c)))for x,y in((0,1),(1,0),(0,-1),(-1,0))if-1<(r:=u[0]+x)<m and-1<(c:=u[1]+y)<n]),u==(m-1,n-1)and h>p[0])[-1]for _ in range(m*n*5))

test('''
3286. Find a Safe Walk Through a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.


Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.


Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
2 <= m * n
1 <= health <= m + n
grid[i][j] is either 0 or 1.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
37,951/112.6K
Acceptance Rate
33.7%
Topics
Staff
Array
Breadth-First Search
Graph Theory
Heap (Priority Queue)
Matrix
Shortest Path
Biweekly Contest 139
icon
Companies
Hint 1
Use 01 BFS.
Similar Questions
Shortest Path in a Grid with Obstacles Elimination
Hard
''')
