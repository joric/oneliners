from lc import *

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        shortestPath, allVisited = float("inf"), (1 << len(graph)) - 1
        for u in range(len(graph)):
            queue, seen, lvl= [(u,  (1 << u))], set([(u,  (1 << u))]), 0
            while queue:
                if any(nodeVisited == allVisited for _, nodeVisited in queue): shortestPath, queue = min(shortestPath, lvl), []
                else: queue, lvl = [(v, nodeVisited | (1 << v)) for u, nodeVisited in queue for v in graph[u] if (v,nodeVisited | (1 << v))  not in seen and not seen.add((v, nodeVisited | (1 << v)))], lvl + 1
        return shortestPath


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        m, f, q = set(), (1 << len(graph)) - 1, [(0, i, 1 << i) for i in range(len(graph))]
        while q:
            s,x,t = heappop(q)
            if t==f:
                return s
            for v in graph[x]:
                if (t | 1 << v, v) not in m:
                    heappush(q, (s + 1, v, t | 1 << v))
                    m.add((t | 1 << v, v))

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        (m:=set(),f:=(1<<len(graph))-1,q:=[(0,i,1<<i) for i in range(len(graph))])
        g=lambda s,x,t:s if t==f else any(heappush(q,(s+1,v,t|1<<v)) or m.add((t|1<<v,v)) for v in graph[x] if (t|1<<v,v) not in m)
        while q:
            if (s:=g(*heappop(q))):
                break
        return s


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        return next((s for _ in count() if not q or (s:=(lambda s,x,t:s if t==f else any(heappush(q,(s+1,v,t|1<<v)) or m.add((t|1<<v,v)) for v in graph[x] if (t|1<<v,v) not in m))(*heappop(q)))),(m:=set(),f:=(1<<len(graph))-1,q:=[(0,i,1<<i) for i in range(len(graph))]))

# deque (longer)

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        return next((s for _ in count() if not q or (s:=(lambda s,x,t:s if t==f else any(q.append((s+1,v,t|1<<v)) or m.add((t|1<<v,v)) for v in graph[x] if (t|1<<v,v) not in m))(*q.popleft()))),(m:=set(),f:=(1<<len(graph))-1,q:=deque([(0,i,1<<i) for i in range(len(graph))])))


test('''

847. Shortest Path Visiting All Nodes
Hard

3124

136

Add to List

Share
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Example 2:
Input: graph = [[]]
Output: 0
 

Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
Accepted
68,701
Submissions
112,592



''')
