from lc import *

# https://leetcode.com/problems/shortest-bridge/discuss/1251709/BFS-python-with-explanation-amazing-solution
# paint a single island as 2, then start incrementing value and expanding from last value until we meet 1, difference would be the shortest bridge
# given there are exactly two islands on the map, the bridge will allways be the shortest

class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        n = len(g)
        def f(i,j):
            if 0<=i<n and 0<=j<n and g[i][j]==1:
                g[i][j] = 2
                [*map(f,(i-1,i+1,i,i),(j,j,j-1,j+1))]

        next(f(i,j) for i in range(n) for j in range(n) if g[i][j]==1)

        def e(i,j,t):
            if 0<=i<n and 0<=j<n:
                if g[i][j]==0:
                    g[i][j] = t+1
                return g[i][j]==1

        t = 2
        while True:
            for i in range(n):
                for j in range(n):
                    if g[i][j]==t and (e(i-1,j,t) or e(i+1,j,t) or e(i,j+1,t) or e(i,j-1,t)):
                        return t-2
            t += 1

class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        n,t=len(g),2
        f = lambda i,j:0<=i<n and 0<=j<n and g[i][j]==1 and (setitem(g[i],j,2),[*map(f,(i-1,i+1,i,i),(j,j,j-1,j+1))])
        e = lambda i,j,t:0<=i<n and 0<=j<n and (g[i][j]==0 and setitem(g[i],j,t+1) or g[i][j]==1)
        next(f(i,j) for i in range(n) for j in range(n) if g[i][j]==1)
        return next(t-2 for _ in count() if next((1 for i in range(n) for j in range(n) if g[i][j]==t and any(map(e,(i-1,i+1,i,i),(j,j,j+1,j-1),[t]*4))),0) or not (t:=t+1))

class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        g = {i+j*1j:x for i,r in enumerate(g) for j,x in enumerate(r)}
        t = 2
        f = lambda z:g.get(z,0)==1 and (setitem(g,z,2),[f(z+1j**k) for k in range(4)])
        e = lambda z,t:z in g and(g[z]==0 and setitem(g,z,t+1) or g[z]==1)
        next(f(z)for z in g if g[z]==1)
        return next(t-2 for _ in count() if next((1 for z in g if g[z]==t and any(e(z+1j**k,t)for k in range(4))),0) or not (t:=t+1))

class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        g,t,f,e={i+j*1j:x for i,r in enumerate(g)for j,x in enumerate(r)},2,lambda z:g.get(z,0)==1 and(setitem(g,z,2),[f(z+1j**k)for k in range(4)]),lambda z,t:z in g and(g[z]==0 and setitem(g,z,t+1)or g[z]==1);next(f(z)for z in g if g[z]==1);return next(t-2 for _ in count()if next((1 for z in g if g[z]==t and any(e(z+1j**k,t)for k in range(4))),0)or not(t:=t+1))


# https://leetcode.com/problems/shortest-bridge/discuss/189489/concise-C%2B%2B-dfs-solution.
# groups approach, borderline TLE
class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        n,a,b = len(g),[],[]
        def f(i,j,p):
            if 0<=i<n and 0<=j<n and g[i][j]==1:
                g[i][j] = 0
                p.append((i,j))
                for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    f(x,y,p)
        for i in range(n):
            for j in range(n):
                f(i,j,b if a else a)
        return min(abs(u[0]-v[0])+abs(u[1]-v[1])-1 for u in a for v in b)

# same for complex numbers (TLE)
class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        g,a,b={i+j*1j:x for i,r in enumerate(g) for j,x in enumerate(r)},[],[]
        f=lambda z:g.get(z,0) and (setitem(g,z,0),p.append(z),[f(z+1j**k) for k in range(4)])
        [(p:=(a,b)[not b],f(z)) for z in g]
        return int(min(abs(u.real-v.real)+abs(u.imag-v.imag)-1 for u in a for v in b))

# one-liner, borderline TLE (8037 ms)
class Solution:
    def shortestBridge(self, g: List[List[int]]) -> int:
        n,a,b,f=len(g),[],[],lambda i,j:n>i>=0<=j<n and g[i][j]and(setitem(g[i],j,0),p.append((i,j)),[*map(f,(i-1,i+1,i,i),(j,j,j-1,j+1))]);r=range(n);[(p:=(a,b)[not b],f(i,j))for i in r for j in r];return min(abs(u[0]-v[0])+abs(u[1]-v[1])-1 for u in a for v in b)

test('''
934. Shortest Bridge
Medium

3927

158

Add to List

Share
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
Accepted
137,196
Submissions
247,882
''')

