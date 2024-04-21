from lc import *
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def validPath(self, n: int, e: List[List[int]], s: int, d: int) -> bool:
        return (g:=defaultdict(list),[{g[a].append(b), g[b].append(a)} for a,b in e]) and (f:=lambda r,o,v: max((f(g,v.add(k) or k,v) for k in r[o] if k not in v), default=0) if o!=d else 1)(g,s,set({s}))

# updated 2024-04-21

# unicode find (TLE)
class Solution:
    def validPath(self, n: int, e: List[List[int]], s: int, d: int) -> bool:
        t = ''.join(map(chr, range(n)))
        for u,v in e:
            t = t.replace(t[u],t[v])
        return t[s]==t[d]

# https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/2927837/Python-BFS-DFS-(explained)-%2B-BONUS-4-LINES-UNION-FIND

class Solution:
    def validPath(self, n: int, e: List[List[int]], s: int, d: int) -> bool:
        p=[*range(n)];f=lambda x:x if x==p[x]else f(p[x]);[setitem(p,f(u),f(v))for u,v in e];return f(d)==f(s)

class Solution:
    def validPath(self, n: int, e: List[List[int]], s: int, d: int) -> bool:
        p={};f=lambda x:f(p[x])if x-p.get(x,x)else x;[setitem(p,f(u),f(v))for u,v in e];return f(d)==f(s)

test('''
1971. Find if Path Exists in Graph
Easy

1847

99

Add to List

Share
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Other examples:

Input: n = 6, edges = [[0,4]], source = 0, destination = 4
Output: true

Constraints:

1 <= n <= 2 * 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.

''')

