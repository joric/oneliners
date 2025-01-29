from lc import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.p = list(range(n))

            def find(self, x):
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, x, y):
                xr = self.find(x)
                yr = self.find(y)
                self.p[xr] = yr
        n = len(set(chain(*edges)))
        dsu = DSU(n)
        for i, j in edges:
            if dsu.find(i-1) == dsu.find(j-1):
                return([i,j])
            else:
                dsu.union(i-1,j-1)

# unicode find: https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        t = ''.join(map(chr, range(1001)))
        for u,v in edges:
            if t[u]==t[v]:
                return [u,v]
            t = t.replace(t[u],t[v])

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        t=''.join(map(chr,range(1001)));return next((u,v) for u,v in edges if t[u]==t[v]or not(t:=t.replace(t[u],t[v])))

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        t=''.join(map(chr,range(1001)));return next((u,v)for u,v in edges if(t[u]==t[v],t:=t.replace(t[u],t[v]))[0])

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        t=''.join(map(chr,range(1001)));return next((u,v)for u,v in edges if(t[u]==t[v],t:=t.replace(t[u],t[v]))[0])

class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        t=''.join(map(chr,range(1001)));return next((u,v)for u,v in e if(t[u]==t[v],t:=t.replace(t[u],t[v]))[0])

class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        t=''.join(map(chr,range(1001)));return next((u,v)for u,v in e if t[u]==(t:=t.replace(t[u],t[v]))[u])

test('''
684. Redundant Connection
Medium

5409

356

Add to List

Share
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
''')