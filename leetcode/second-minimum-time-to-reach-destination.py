from lc import *

# https://leetcode.com/problems/second-minimum-time-to-reach-destination/discuss/4833209/Python3-Modified-Dijkstra-Simple-Solution

class Solution:
    def secondMinimum(self, n: int, e: List[List[int]], m: int, c: int) -> int:
        g = defaultdict(list)
        for u,v in e:
            g[u].append(v)
            g[v].append(u)
        d = [[inf,inf] for _ in range(n+1)]
        q = [(0,1)]
        while q:
            t,u = heappop(q)
            if u==n and d[u][1] != inf:
                return d[u][1]
            k = m
            if (t // c) % 2 == 1:
                k += (t // c + 1) * c - t
            for v in g[u]:
                if k+t < d[v][0]:
                    d[v][0], d[v][1] = k + t, d[v][0]
                    heappush(q,(k+t,v))
                if d[v][0] < k+t < d[v][1]:
                    d[v][1] = k+t
                    heappush(q, (k+t, v))
        return -1

# https://leetcode.com/problems/second-minimum-time-to-reach-destination/discuss/1525149/Python-Modified-Dijkstra-explained

class Solution:
    def secondMinimum(self, n: int, e: List[List[int]], t: int, c: int) -> int:
        g,d=[defaultdict(list)for _ in(0,1)]
        d[1] = [0]
        q = [(0,1)]
        for u,v in e:
            g[u].append(v)
            g[v].append(u)
        while q:
            m,u = heappop(q)
            if u==n and len(d[n]) == 2:
                return max(d[n])
            w = t+(m,ceil(m/(2*c))*(2*c) ) [(m//c)%2]
            for v in g[u]:
                if not d[v] or (len(d[v]) == 1 and d[v] != [w]):
                    d[v] += [w]
                    heappush(q, (w,v))

class Solution:
    def secondMinimum(self, n: int, e: List[List[int]], t: int, c: int) -> int:
        g,d=[defaultdict(list)for _ in(0,1)];[g[u].append(v)==g[v].append(u)for u,v in e];d[1].append(0);q=[(0,1)];return next(max(d[n])for _ in count()if(p:=heappop(q),m:=p[0],u:=p[1])and(2==len(d[n])and u==n)or(w:=t+(m,ceil(m/(2*c))*(2*c))[(m//c)%2],[(not d[v]or(1==len(d[v])and[w]!=d[v]))and d[v].append(w)==heappush(q,(w,v))for v in g[u]])==0)

test('''
2045. Second Minimum Time to Reach Destination
Hard

703

13

Add to List

Share
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
 

Example 1:

        
Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.      
Example 2:


Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.
 

Constraints:

2 <= n <= 104
n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
There are no duplicate edges.
Each vertex can be reached directly or indirectly from every other vertex.
1 <= time, change <= 103
Accepted
11,987
Submissions
29,167
''')
