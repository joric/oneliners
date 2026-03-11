from lc import *

# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/solutions/6899301/python-kruskal-two-pass-by-awice-tbd5/?envType=daily-question&envId=2026-03-12

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        used = 0
        ans = inf
        dsu = DSU(n)

        for u, v, s, m in edges:
            if m:
                if not dsu.union(u, v):
                    return -1
                used += 1
                ans = min(ans, s)

        edges.sort(key=lambda e: -e[2])
        weights = []
        for u, v, s, m in edges:
            if m == 0:
                if dsu.union(u, v):
                    used += 1
                    weights.append(s)

        for i in range(min(k, len(weights))):
            weights[~i] *= 2

        if used != n - 1:
            return -1
        return min((ans, *weights))

class Solution:
    def maxStability(self, n: int, e: List[List[int]], k: int) -> int:
        c = 0
        r = inf
        t = ''.join(map(chr, range(n + 1)))

        for u,v,s,m in e:
            if m:
                if t[u] == t[v]:
                    return -1
                t = t.replace(t[u], t[v])
                c += 1
                r = min(r, s)

        e.sort(key=lambda p: -p[2])
        w = []

        for u, v, s, m in e:
            if m == 0:
                if t[u] != t[v]:
                    t = t.replace(t[u], t[v])
                    c += 1
                    w.append(s)

        for i in range(min(k,len(w))):
            w[~i] *= 2
        if c != n - 1:
            return -1
        return min((r,*w))

class Solution:
    def maxStability(self, n:int, e:List[List[int]], k:int)->int:
        c,r,t=0,inf,''.join(map(chr,range(n+1)));b=all(t[u]!=t[v]and(t:=t.replace(t[u],t[v]),c:=c+1,r:=min(r,s))for u,v,s,m in e if m);w=[s for u,v,s,m in sorted(e,key=lambda p:-p[2])if m<1and t[u]!=t[v]and(t:=t.replace(t[u],t[v]),c:=c+1)];return(-1,min([r]+[x<<(i>=len(w)-k)for i,x in enumerate(w)]))[b and c+1==n]

class Solution:
    def maxStability(self, n:int, e:List[List[int]], k:int)->int:
        c,r,t,w=0,inf,''.join(map(chr,range(n+1))),[];b=all(t[u]!=t[v]and(t:=t.replace(t[u],t[v]),c:=c+1,m and(r:=min(r,s)),m<1and w.append(s))for u,v,s,m in sorted(e,key=lambda p:(p[3]<1,-p[2]))if m or t[u]!=t[v]);return(-1,min([r]+[x<<(i>=len(w)-k)for i,x in enumerate(w)]))[b and c==n-1]

class Solution:
    def maxStability(self, n:int, e:List[List[int]], k:int)->int:
        c,r,t,w=0,inf,''.join(map(chr,range(n+1))),[];b=all(t[u]!=t[v]and(t:=t.replace(t[u],t[v]),c:=c+1,m and(r:=min(r,s)),m or w.append(s))for u,v,s,m in sorted(e,key=lambda p:(-p[3],-p[2]))if m or t[u]!=t[v]);return(-1,min([r]+[x<<(i>=len(w)-k)for i,x in enumerate(w)]))[b and c==n-1]

class Solution:
    def maxStability(self, n:int, e:List[List[int]], k:int)->int:
        c,t,w=0,''.join(map(chr,range(n+1))),[];b=all(t[u]!=t[v]and(t:=t.replace(t[u],t[v]),c:=c+1,m or w.append(s))for u,v,s,m in sorted(e,key=lambda p:(-p[3],-p[2]))if m or t[u]!=t[v]);return(-1,min([s for*_,s,m in e if m]+[x<<(i>=len(w)-k)for i,x in enumerate(w)]))[b and c==n-1]

class Solution:
    def maxStability(self, n:int, e:List[List[int]], k:int)->int:
        c,t=1,''.join(map(chr,range(n+1)));w=[s for u,v,s,m in sorted(e,key=lambda p:(-p[3],-p[2]))if(t[u]!=t[v]and(t:=t.replace(t[u],t[v]),c:=c+1)or(c:=c-m)<c)and m<1];return(min([s for*_,s,m in e if m]+[x<<(i<k)for i,x in enumerate(w[::-1])]),-1)[c<n]

test('''
3600. Maximize Spanning Tree Stability with Upgrades
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:

ui and vi indicates an undirected edge between nodes ui and vi.
si is the strength of the edge.
musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.
You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.

The stability of a spanning tree is defined as the minimum strength score among all edges included in it.

Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.

Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.

 

Example 1:

Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1

Output: 2

Explanation:

Edge [0,1] with strength = 2 must be included in the spanning tree.
Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
The resulting spanning tree includes these two edges with strengths 2 and 6.
The minimum strength in the spanning tree is 2, which is the maximum possible stability.
Example 2:

Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2

Output: 6

Explanation:

Since all edges are optional and up to k = 2 upgrades are allowed.
Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
The resulting spanning tree includes these two edges with strengths 8 and 6.
The minimum strength in the tree is 6, which is the maximum possible stability.
Example 3:

Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0

Output: -1

Explanation:

All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.

Other examples:

Input: n = 3, edges = [[0,1,55839,0],[0,2,39867,0],[1,2,62840,0]], k = 1
Output: 62840

Input: n = 5, edges = [[2,0,68643,1],[1,0,31681,1],[4,2,44760,1],[3,4,19034,1],[1,4,24247,0]], k = 2
Output: 19034

Constraints:

2 <= n <= 105
1 <= edges.length <= 105
edges[i] = [ui, vi, si, musti]
0 <= ui, vi < n
ui != vi
1 <= si <= 105
musti is either 0 or 1.
0 <= k <= n
There are no duplicate edges.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
7,324/18.4K
Acceptance Rate
39.9%
Topics
Senior Staff
Binary Search
Greedy
Union-Find
Graph Theory
Minimum Spanning Tree
Weekly Contest 456
icon
Companies
Hint 1
Sort the edges array in descending order of weights.
Hint 2
Try using binary search on ans.
Hint 3
Implement a chk function which first adds all the edges with must = 1, and then adds the edges with must = 0, using any remaining upgrades greedily.
Hint 4
Use a DSU with path compression and union by size/rank to maintain connected components.
Hint 5
Don't forget the case where you cannot form an MST because more than one component remains after processing all edges.
''')
