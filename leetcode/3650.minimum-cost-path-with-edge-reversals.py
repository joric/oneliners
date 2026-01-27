from lc import *

# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/solutions/7089317/dijkstras-algorithm-python3-by-cinderace-yd5q/?envType=daily-question&envId=2026-01-27

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for start, end, weight in edges:
            d[start].append((end, weight))
            d[end].append((start, 2 * weight))
        minheap = [(0, 0)]
        seen = set()
        while minheap:
            score, curr = heappop(minheap)
            if curr == n - 1:
                return score
            if curr in seen:
                continue
            seen.add(curr)
            for nei, s in d[curr]:
                if nei not in seen:
                    heappush(minheap, (score + s, nei))
        return -1

class Solution:
    def minCost(self, n: int, g: List[List[int]]) -> int:
        d = defaultdict(list)
        for s,e,w in g:
            d[s].append((e,w))
            d[e].append((s,2*w))
        h = [(0,0)]
        v = set()
        while h:
            s,c = heappop(h)
            if c == n - 1:
                return s
            if c in v:
                continue
            v.add(c)
            for i,j in d[c]:
                if i not in v:
                    heappush(h,(s+j,i))
        return -1

class Solution:
    def minCost(self, n: int, g: List[List[int]]) -> int:
        d=defaultdict(list)
        for s,e,w in g:
            d[s].append((e,w))
            d[e].append((s,2*w))
        h=[(0,0)]
        v={-1}
        while h:
            s,u=heappop(h)
            if u==n-1:
                return s
            if{u}-v:
                v.add(u)
                [heappush(h,(s+w,t))for t,w in d[u]]
        return -1

class Solution:
    def minCost(self, n: int, g: List[List[int]]) -> int:
        d=defaultdict(list);[d[s].append((e,w))or d[e].append((s,2*w))for s,e,w in g];h,v=[],set();return(f:=lambda s,c:s if c==n-1 else[c not in v and(v.add(c),[heappush(h,(s+j,i))for i,j in d[c]if i not in v]),h and f(*heappop(h))][1]or-1)(0,0)

class Solution:
    def minCost(self, n: int, g: List[List[int]]) -> int:
        d=defaultdict(list);[d[s].append((e,w))or d[e].append((s,2*w))for s,e,w in g];h,v=[],set();return(f:=lambda s,u:u+2>n and s or(u in v or(v.add(u),[heappush(h,(s+w,t))for t,w in d[u]]),h and f(*heappop(h)))[1]or-1)(0,0)

test('''
3650. Minimum Cost Path with Edge Reversals
Medium
Topics
premium lock icon
Companies
Hint
You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

 

Example 1:

Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

Output: 5

Explanation:



Use the path 0 → 1 (cost 3).
At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
Total cost is 3 + 2 = 5.
Example 2:

Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

Output: 3

Explanation:

No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
Total cost is 1 + 1 + 1 = 3.

Other examples:

Input: n = 3, edges = [[2,0,12],[1,0,5],[0,1,15]]
Output: 24


Input: n = 4, edges = [[2,3,25],[2,1,18],[3,1,2]]
Output: -1

Input: n = 5, edges = [[1,2,8],[3,1,10],[0,3,3]]
Output: -1

Constraints:

2 <= n <= 5 * 104
1 <= edges.length <= 105
edges[i] = [ui, vi, wi]
0 <= ui, vi <= n - 1
1 <= wi <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
15,905/33.5K
Acceptance Rate
47.4%
Topics
Graph Theory
Heap (Priority Queue)
Shortest Path
Biweekly Contest 163
icon
Companies
Hint 1
Do we only need to reverse at most one edge for each node? If so, can we add reversed edges for each node and use the one that helps in the shortest path?
Hint 2
Add reverse edges: {u, v, w} -> {v, u, 2 * w}, and use Dijkstra.
Similar Questions
Minimum Cost to Reach Destination in Time
Hard
''')
