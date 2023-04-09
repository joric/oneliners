from lc import *

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        d = [0]*(n:=len(colors))
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            d[v] += 1
        q = [u for u in range(n) if d[u]==0]
        c = [[0]*26 for _ in range(n)]
        for u in q:
            c[u][ord(colors[u])-ord('a')] += 1
            for v in g[u]:
                c[v] = list(map(max,c[v],c[u]))
                d[v] -= 1
                if d[v]==0:
                    q.append(v)
        return -1 if len(q)<n else max(max(x) for x in c)

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        return (n:=len(colors),d:=[0]*n,g:=[[] for _ in range(n)],[(g[u].append(v),setitem(d,v,d[v]+1)) for u, v in edges],q:=[u for u in range(n) if d[u]==0],c:=[[0]*26 for _ in range(n)],[(t:=ord(colors[u])-ord('a'),setitem(c[u],t,c[u][t]+1),[(setitem(c,v,[*map(max,c[v],c[u])]),setitem(d,v,d[v]-1),d[v]==0 and q.append(v)) for v in g[u]]) for u in q],-1 if len(q)<n else max(max(x) for x in c))[-1]

test('''
1857. Largest Color Value in a Directed Graph
Hard

845

30

Add to List

Share
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 10^5
0 <= m <= 10^5
colors consists of lowercase English letters.
0 <= aj, bj < n
Accepted
20,464
Submissions
46,296
Seen this question in a real interview before?

Yes

No
Use topological sort.
let dp[u][c] := the maximum count of vertices with color c of any path starting from vertex u. (by JerryJin2905)
''')

