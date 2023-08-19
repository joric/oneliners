from lc import *

# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/discuss/735619/C%2B%2B-Dijkstra's-Minimax-Path-Algorithm

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, e: List[List[int]]) -> List[List[int]]:
        g,r=defaultdict(list),[[],[]]
        for u,v,w in e:
            g[u].append((v,w))
            g[v].append((u,w))
        def f(a,b):
            d = [inf]*len(g)
            q = deque([(0,a)])
            d[a] = 0
            while q:
                p,u = q.popleft()
                if -p>d[u]:
                    continue
                for v,w in g[u]:
                    if (u!=a or v!=b) and d[v]>max(d[u],w):
                        d[v] = max(d[u],w)
                        q.append((-d[v],v))
            return d[b]
        for i,(u,v,w) in enumerate(e):
            m = f(u,v)
            if m>w:
                r[0].append(i)
            elif m==w:
                r[1].append(i)
        return r

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, e: List[List[int]]) -> List[List[int]]:
        g,r=defaultdict(list),[[],[]]
        any(g[u].append((v,w)) or g[v].append((u,w)) for u,v,w in e)
        def f(a,b):
            d = [inf]*len(g)
            q = deque([(0,a)])
            d[a] = 0
            while q:
                p,u = q.popleft()
                any(setitem(d,v,max(d[u],w)) or q.append((-d[v],v)) for v,w in g[u] if -p<=d[u] and (u!=a or v!=b) and d[v]>max(d[u],w))
            return d[b]
        any(r[w==m].append(i) for i,(u,v,w) in enumerate(e) if (m:=f(u,v))>=w)
        return r

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, e: List[List[int]]) -> List[List[int]]:
        g,r=defaultdict(list),[[],[]]
        any(g[u].append((v,w)) or g[v].append((u,w)) for u,v,w in e)
        f=lambda a,b:next((d[b] for _ in count() if not(q and not(lambda p,u:any(setitem(d,v,max(d[u],w)) or q.append((-d[v],v)) for v,w in g[u] if -p<=d[u] and (u!=a or v!=b) and d[v]>max(d[u],w)))(*q.popleft()))),(d:=[inf]*len(g),q:=deque([(0,a)]),setitem(d,a,0)))
        any(r[w==m].append(i) for i,(u,v,w) in enumerate(e) if (m:=f(u,v))>=w)
        return r

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, e: List[List[int]]) -> List[List[int]]:
        g,r=defaultdict(list),[[],[]];[(g[u].append((v,w)),g[v].append((u,w)))for u,v,w in e];f=lambda a,b:next((d[b]for _ in count()if not(q and(lambda p,u:all((setitem(d,v,max(d[u],w)),q.append((-d[v],v)))for v,w in g[u]if -p<=d[u]and(u!=a or v!=b)and d[v]>max(d[u],w)))(*q.popleft()))),(d:=[inf]*len(g),q:=deque([(0,a)]),setitem(d,a,0)));[r[w==m].append(i)for i,(u,v,w)in enumerate(e)if(m:=f(u,v))>=w];return r

test('''
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
Hard

885

76

Add to List

Share
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:



Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:



Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.
''')

