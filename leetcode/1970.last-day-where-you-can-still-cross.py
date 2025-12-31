from lc import *

# https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/3214413/Python-Clean-DSU-or-O(N*M)-15-lines

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        class DSU:
            def __init__(self, N):
                self.v = list(range(N))
                self.sizes = [1] * N

            def find(self, x):
                if self.v[x] != x:
                    self.v[x] = self.find(self.v[x])
                return self.v[x]

            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)
                if px != py:
                    if self.sizes[px] < self.sizes[py]:
                        px, py = py, px
                    self.sizes[px] += self.sizes[py]
                    self.v[py] = px
        ds = DSU(row*col + 2)
        for i in range(row): 
            ds.union(0,i*col + 1)
            ds.union(row*col+1,i*col + col)
        water = set()
        for days,(r,c) in enumerate(cells):
            water.add((r-1,c-1))
            for dy,dx in [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,-1),(-1,1),(1,1)]:
                    y,x = dy+r-1,dx+c-1
                    if(x>=0 and y>=0 and x<col and y<row and (y,x) in water):
                        ds.union((r-1)*col+c -1 + 1,y*col + x+1)
            if(ds.find(0)==ds.find(row*col+1)): return days
        return len(cells)

# https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1440354/Python-Binary-Search

class Solution:
    def latestDayToCross(self, m: int, n: int, c: List[List[int]]) -> int:
        def f(k):
            a=[[0]*n for _ in range(m)]
            for i in range(k):
                a[c[i][0]-1][c[i][1]-1]=1
            q=deque()
            v=set()
            for j in range(n):
                if a[0][j]==0:
                    q.append((0,j))
                    v.add((0,j))
            while q:
                i,j=q.popleft()
                if i==m-1:
                    return True
                for x,y in ((i,j+1),(i,j-1),(i+1,j),(i-1,j)):
                    if (x,y) not in v and m>x>=0<=y<n and a[x][y]==0:
                        q.append((x,y))
                        v.add((x,y))
            return False
        l,h=0,m*n
        while l<h:
            d=l+(h-l+1)//2
            if f(d):
                l=d
            else:
                h=d-1
        return l

class Solution:
    def latestDayToCross(self, m: int, n: int, c: List[List[int]]) -> int:
        f=lambda k:(r:=1,a:=[[0]*n for _ in range(m)],v:=set(),q:=deque(),[setitem(a[c[i][0]-1],c[i][1]-1,1) for i in range(k)],[a[0][j]==0 and(q.append((0,j)),v.add((0,j)))for j in range(n)])and next(not r for _ in count() if not(q and r and(w:=[],[[(x,y)not in v and m>x>=0<=y<n and a[x][y]==0 and(w.append((x,y)),v.add((x,y)))for x,y in((i,j+1),(i,j-1),(i+1,j),(i-1,j))if r and(r:=i!=m-1)]for i,j in q],q:=w)));l,h=0,m*n;return next(l for _ in count()if not(l<h and(d:=l+(h-l+1)//2,(l:=d)if f(d)else(h:=d-1))))

# unicode find

class Solution:
    def latestDayToCross(self, s: int, t: int, m: List[List[int]]) -> int:
        u=''.join(map(chr,range(s*t+2)))
        for i in range(s): 
            u = u.replace(u[0],u[i*t+1]).replace(u[-1],u[i*t+t])
        w = set()
        for d, (r,c) in enumerate(m):
            w.add((r-1,c-1))
            for i,j in product([-1,0,1],[-1,0,1]):
                x,y = i+r-1,j+c-1
                if s>y>=0<=x<t and (y,x) in w:
                    u = u.replace(u[(r-1)*t+c], u[y*t+x+1])
            if u[0]==u[-1]:
                return d
        return len(m)

class Solution:
    def latestDayToCross(self, s: int, t: int, m: List[List[int]]) -> int:
        u,w=''.join(map(chr,range(s*t+2))),set();[(u:=u.replace(u[0],u[i*t+1]).replace(u[-1],u[i*t+t]))for i in range(s)];return next(d for d,(r,c)in enumerate(m)if not((w.add((r-1,c-1)),[(x:=j+c-1,y:=i+r-1,s>y>=0<=x<t and(y,x)in w and(u:=u.replace(u[(r-1)*t+c],u[y*t+x+1])))for i,j in product([-1,0,1],[-1,0,1])])and u[0]!=u[-1]))

class Solution:
    def latestDayToCross(self, s: int, t: int, m: List[List[int]]) -> int:
        f=lambda u,x,y:u.replace(u[x],u[y]);u,w=''.join(map(chr,range(s*t+2))),set();[(u:=f(f(u,0,i*t+1),-1,i*t+t))for i in range(s)];return next(d for d,(r,c)in enumerate(m)if not((w.add((r-1,c-1)),[(x:=j+c-1,y:=i+r-1,s>y>=0<=x<t and(y,x)in w and(u:=f(u,(r-1)*t+c,y*t+x+1)))for i,j in product(*[[-1,0,1]]*2)])and u[0]!=u[-1]))

class Solution:
    def latestDayToCross(self, s: int, t: int, m: List[List[int]]) -> int:
        v,z="".join,range;u,w=f'A{v("A"+v(chr(r*t+c+67)for c in z(t-2))+"B"for r in z(s))}B',set();return next(d for d,(r,c)in enumerate(m)if not((w.add((r-1,c-1)),[(x:=j+c-1,y:=i+r-1,s>y>=0<=x<t and(y,x)in w and(u:=u.replace(u[(r-1)*t+c],u[y*t+x+1])))for i,j in product(*[[-1,0,1]]*2)])and u[0]!=u[-1]))

# 2025-12-31 POTD

class Solution:
    def latestDayToCross(self, r: int, c: int, s: List[List[int]]) -> int:
        v,j=range,"".join;u=j(f'A{j(chr(i*c+k+67)for k in v(c-2))}B'for i in v(r));w=set();return next(i for i,(p,q)in enumerate(s)if(x:=p-1,y:=q-1,w.add((x,y)),[(b:=d+x,a:=e+y,r>b>=0<=a<c and(b,a)in w and(u:=u.replace(u[x*c+y],u[b*c+a])))for d,e in product(*[[-1,0,1]]*2)])and u[0]==u[-1])

class Solution:
    def latestDayToCross(self, r: int, c: int, s: List[List[int]]) -> int:
        v,j=range,''.join;u=j(f'A{j(chr(i*c+k+67)for k in v(c-2))}B'for i in v(r));w=set();return next(i for i,(p,q)in enumerate(s)if(x:=p-1,y:=q-1,w.add((x,y)),[((b:=d+x,a:=e+y)in w and(r>b>=0<=a<c)and(u:=u.replace(u[x*c+y],u[b*c+a])))for d,e in product(*[[-1,0,1]]*2)])and u[0]==u[-1])

class Solution:
    def latestDayToCross(self, r: int, c: int, s: List[List[int]]) -> int:
        w,v,j=set(),range,''.join;u=j(f'A{j(chr(i*c+k+67)for k in v(c-2))}B'for i in v(r));return next(i for i,(p,q)in enumerate(s)if(x:=p-1,y:=q-1,w.add((x,y)),[((b:=d+x,a:=e+y)in w and r>b>=0<=a<c!=(u:=u.replace(u[x*c+y],u[b*c+a])))for d,e in product(*[[-1,0,1]]*2)])!=u[0]==u[-1])

class Solution:
    def latestDayToCross(self, r: int, c: int, s: List[List[int]]) -> int:
        w,v,j=set(),range,''.join;u=j(f'A{j(chr(i*c+k+67)for k in v(c-2))}B'for i in v(r));return next(i for i,(p,q)in enumerate(s)if(w.add((x:=p-1,y:=q-1)),[r>b>-1<a<c!=(b,a)in w and(u:=u.replace(u[x*c+y],u[b*c+a]))for b in v(x-1,x+2)for a in v(y-1,y+2)])!=u[0]==u[-1])

test('''
1970. Last Day Where You Can Still Cross
Hard

670

13

Add to List

Share
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
 

Constraints:

2 <= row, col <= 2 * 10^4
4 <= row * col <= 2 * 10^4
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
Accepted
13,521
Submissions
26,320
Seen this question in a real interview before?

Yes

No
Bricks Falling When Hit
Hard
Escape the Spreading Fire
Hard
What graph algorithm allows us to find whether a path exists?
Can we use binary search to help us solve the problem?
''')
