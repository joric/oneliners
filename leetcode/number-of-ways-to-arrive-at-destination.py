from lc import *

# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/discuss/1417573/python-Almost-Dijktra-explained

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        G = defaultdict(list)
        for x, y, w in roads:
            G[x].append((y, w))
            G[y].append((x, w))
        dist = [inf] * n
        dist[0] = 0
        cnt = [0]*n
        cnt[0] = 1
        heap = [(0, 0)]
        while heap:
            (min_dist, idx) = heappop(heap)
            if idx == n-1:
                return cnt[idx] % (10**9 + 7)
            for neib, weight in G[idx]:
                candidate = min_dist + weight
                if candidate == dist[neib]:
                    cnt[neib] += cnt[idx]
                elif candidate < dist[neib]:
                    dist[neib] = candidate
                    heappush(heap, (weight + min_dist, neib))
                    cnt[neib] = cnt[idx]

# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/discuss/1417576/C%2B%2BPython-Dijkstra-Clean-and-Concise

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)

# let's do priority queue here
from queue import PriorityQueue

class Solution:
    def countPaths(self, n: int, r: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v,t in r:
            g[u].append([v,t])
            g[v].append([u,t])
        p = [0]+[inf]*(n-1)
        c = [1]+[0]*(n-1)
        q = PriorityQueue()
        q.put((0,0))
        while not q.empty():
            d,u = q.get()
            if p[u]<d:
                continue
            for v,t in g[u]:
                if p[v] > d + t:
                    p[v] = d + t
                    c[v] = c[u]
                    q.put((p[v],v))
                elif p[v] == d+t:
                    c[v] = (c[v]+c[u])%(10**9+7)
        return c[n-1]


# shorten a bit

class Solution:
    def countPaths(self, n: int, r: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v,t in r:
            g[u].append([v,t])
            g[v].append([u,t])
        p = [0]+[inf]*(n-1)
        c = [1]+[0]*(n-1)
        q = [(0,0)]
        while q:
            d,u = heappop(q)
            if p[u]<d:
                continue
            for v,t in g[u]:
                if p[v] > d + t:
                    p[v] = d + t
                    c[v] = c[u]
                    heappush(q, (p[v],v))
                elif p[v] == d+t:
                    c[v] = (c[v]+c[u])%(10**9+7)
        return c[n-1]

class Solution:
    def countPaths(self, n: int, r: List[List[int]]) -> int:
        g=defaultdict(list);[(g[u].append([v,t]),g[v].append([u,t]))for u,v,t in r]
        p,c,q=[0]+[inf]*(n-1),[1]+[0]*(n-1),[];
        def f(d,u):
            p[u]>=d
            for v,t in g[u]:
                p[v]>d+t and(setitem(p,v,d+t),setitem(c,v,c[u]),heappush(q,(p[v],v)))or p[v]==d+t and setitem(c,v,(c[v]+c[u])%(10**9+7))
            q and f(*heappop(q))
        f(0,0)
        return c[n-1]

class Solution:
    def countPaths(self, n: int, r: List[List[int]]) -> int:
        g=defaultdict(list);[(g[u].append([v,t]),g[v].append([u,t]))for u,v,t in r];p,c,q=[0]+[inf]*(n-1),[1]+[0]*(n-1),[];(f:=lambda d,u:(p[u]>=d and[p[v]>d+t and(setitem(p,v,d+t),setitem(c,v,c[u]),heappush(q,(p[v],v)))or p[v]==d+t and setitem(c,v,(c[v]+c[u])%(10**9+7))for v,t in g[u]])and q and f(*heappop(q)))(0,0);return c[n-1]

test('''
1976. Number of Ways to Arrive at Destination
Medium

2587

111

Add to List

Share
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:


Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 

Constraints:

1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
There is at most one road connecting any two intersections.
You can reach any intersection from any other intersection.
Accepted
50,731
Submissions
179,800
''')

