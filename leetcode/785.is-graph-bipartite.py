from lc import *

# https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        p = {}
        def dfs(x, c):
            if x in p:
                return p[x] == c
            p[x] = c
            return all(dfs(y,-c) for y in graph[x])
        return all(i in p or dfs(i, 1) for i in range(len(graph)))

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        return (p:={}) or all(i in p or (f:=lambda x,c:p[x]==c if x in p else setitem(p,x,c)
            or all(f(y,-c) for y in graph[x]))(i, 1) for i in range(len(graph)))

class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        p={};return all(i in p or (f:=lambda x,c:p[x]==c if x in p else setitem(p,x,c) or all(f(y,-c) for y in g[x]))(i,1) for i in range(len(g)))

class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        t = len(g)
        u = ''.join(map(chr,range(t+1)))
        for i in range(t):
            for j in g[i]:
                if u[i]==u[j]:
                    return False
                u = u.replace(u[j],u[g[i][0]])
        return True

class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        t=len(g);u=''.join(map(chr,range(t+1)));return all(u[i]!=u[j]and(u:=u.replace(u[j],u[g[i][0]]))for i in range(t)for j in g[i])

class Solution:
    def isBipartite(self, g):
        u=''.join(map(chr,range(999)));return all(u[i]!=u[j]and(u:=u.replace(u[j],u[x[0]]))for i,x in enumerate(g)for j in x)

test('''

785. Is Graph Bipartite?
Medium

5703

293

Add to List

Share
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.

''')
