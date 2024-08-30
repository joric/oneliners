from lc import *

# https://leetcode.com/problems/modify-graph-edge-weights/discuss/5711966/simple-python-solution

class Solution:
    def modifiedGraphEdges(self, n: int, e: List[List[int]], s: int, c: int, t: int) -> List[List[int]]:

        def f():
            d = [inf] * n
            d[s] = 0
            q = [(0, s)]

            while q:
                p,u = heappop(q)
                if d[u] < p:
                    continue

                for v, w in g[u]:
                    if w == -1:
                        continue
                    if d[v] > d[u] + w:
                        d[v] = d[u] + w
                        heappush(q, (d[v], v))

            return d[c]

        g = [[] for _ in range(n)]
        for u, v, w in e:
            g[u].append((v,w))
            g[v].append((u,w))

        d = f()

        if d < t:
            return []
        o = d == t
        for i in range(len(e)):
            u, v, w = e[i]
            if w > 0:
                continue
            if o:
                e[i][2] = 2 * 10**9
            else:
                e[i][2] = 1
                g[u].remove((v, -1))
                g[v].remove((u, -1))
                g[u].append((v, 1))
                g[v].append((u, 1))
                d = f()
                if d <= t:
                    o = True
                    e[i][2] += t - d
                g[u].remove((v, 1))
                g[v].remove((u, 1))
                g[u].append((v, e[i][2]))
                g[v].append((u, e[i][2]))
        return e if o else []

class Solution: # FAIL
    def modifiedGraphEdges(self, n: int, e: List[List[int]], s: int, c: int, t: int) -> List[List[int]]:
        g,m = defaultdict(list),setitem
        [g[u].append((v,w))or g[v].append((u,w))for u,v,w in e]
        r,a=lambda u,v,x:(g[u].remove((v,x)),g[v].remove((u,x))),lambda u,v,x:(g[u].append((v,x)),g[v].append((u,x)))
        (j:=lambda:(q:=[],d:=[inf]*n,setitem(d,s,0),(k:=lambda p,u:d[u]>=p and([d[v]>d[u]+w and(setitem(d,v,d[u]+w),heappush(q,(d[v],v)))for v,w in g[u]if w!=-1],q and k(*heappop(q))))(0,s))and d[c])
        if (d:=j())<t: return []
        o = d==t
        [o and m(e[i],2,2*10**9)or(m(e[i],2,1),r(u,v,-1),a(u,v,1),t>=(d:=j())and(o:=1,m(e[i],2,e[i][2]+t-d)),r(u,v,1),a(u,v,e[i][2]))for i,(u,v,w)in enumerate(e)if w<=0]
        return e if o else []

# https://leetcode.com/problems/modify-graph-edge-weights/discuss/3557844/One-By-One

class Solution:
    def modifiedGraphEdges(self, n: int, e: List[List[int]], s: int, d: int, t: int) -> List[List[int]]:
        g = defaultdict(list)
        [g[u].append((v,i))or g[v].append((u,i))for i,(u,v,_)in enumerate(e)]
        def f(m):
            q = []
            x = [inf] * len(g)
            y = [inf] * len(g)
            heappush(q, (0, s))
            x[s] = 0
            while q and q[0][1] != d:
                c, i = heappop(q)
                if c != x[i]:
                    continue
                [(w:=e[k][2],(m or w!=-1)and x[j]>c+max(1,w)and(setitem(y,j,k if w==-1 else y[i]),setitem(x,j,c+max(1,w)),heappush(q,(x[j],j))))for j, k in g[i]]
            return x[d], y[d]
        x, _ = f(False)
        if x < t:
            return []
        while True:
            x, y = f(True)
            if x > t:
                return []
            if x == t:
                break
            e[y][2] = 1 + t - x
        [setitem(z,2,z[2]==-1 and 1 or z[2])for z in e]
        return e

test('''
2699. Modify Graph Edge Weights
Hard

300

59

Add to List

Share
You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.

 

Example 1:



Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4, 1, 1], [2, 0, 1], [0, 3, 1], [4, 3, 3]]

-Output: [[4, 1, 3], [2, 0, 1], [0, 3, 1], [4, 3, 1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
Example 2:



Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
Example 3:



Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
 

Constraints:

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
The graph is connected, and there are no self-loops or repeated edges
Accepted
7,481
Submissions
24,033
''', check=lambda r,e,*args:sorted(r)==sorted(e))
