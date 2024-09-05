from lc import *

# https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/2704866/Python3-or-Concise-15-line-BFS-solution-or-Time-O(n)

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [defaultdict(set), defaultdict(set)]
        q = deque([(0,0,0),(0,0,1)])
        r = [inf]*n
        v = Counter()
        for s,e in redEdges:
            g[0][s].add(e) 
        for s,e in blueEdges:
            g[1][s].add(e)
        while q:
            i,d,c = q.popleft()
            r[i] = min(r[i],d)
            for j in g[c][i]:
                if not v[(j,c)]:
                    v[(j,c)] = 1
                    q.append((j,1+d,1-c))
        return [(x if x<inf else -1) for x in r]

# https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339964/JavaPython-BFS

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[[],[]] for i in range(n)]
        p = [[0,0]] + [[inf,inf] for i in range(n-1)]
        q = [[0,0],[0,1]]
        for i,j in redEdges:
            g[i][0].append(j)
        for i,j in blueEdges:
            g[i][1].append(j)
        for i,c in q:
            for j in g[i][c]:
                if p[j][c] == inf:
                    p[j][c] = p[i][1-c] + 1
                    q.append([j, 1-c])
        return [x if x<inf else -1 for x in map(min,p)]

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[[],[]] for i in range(n)]
        p = [[0,0]] + [[inf,inf] for i in range(n-1)]
        q = [[0,0],[0,1]]
        any(g[i][c].append(j) for c,e in enumerate((redEdges,blueEdges)) for i,j in e)
        any(setitem(p[j],c,p[i][1-c]+1) or q.append([j,1-c]) for i,c in q for j in g[i][c] if p[j][c]==inf)
        return [x if x<inf else -1 for x in map(min,p)]

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        return (g:=[[[],[]] for i in range(n)],p:=[[0,0]]+[[inf,inf] for i in range(n-1)],q:=[[0,0],[0,1]],[g[i][c].append(j) for c,e in enumerate((redEdges,blueEdges)) for i,j in e],[setitem(p[j],c,p[i][1-c]+1) or q.append([j,1-c]) for i,c in q for j in g[i][c] if p[j][c]==inf],[x if x<inf else -1 for x in map(min,p)])[-1]

test('''
1129. Shortest Path with Alternating Colors
Medium

1991

96

Add to List

Share
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Example 3:

Input: n = 3, redEdges = [[0,1],[0,2]], blueEdges = [[1,0]]
Output: [0,1,1]

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
''')
