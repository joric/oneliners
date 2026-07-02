from lc import *

# https://leetcode.com/problems/network-recovery-pathways/editorial/?envType=daily-question&envId=2026-07-03

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        def check(mid: int) -> bool:

            @cache
            def dfs(u: int) -> int:
                if u == n - 1:
                    return 0
                res = float("inf")
                for v, w in g[u]:
                    if w >= mid:
                        res = min(res, dfs(v) + w)
                return res

            return dfs(0) <= k

        if not check(l):
            return -1

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r

class Solution:
    def findMaxPathScore(self, e: List[List[int]], o: List[bool], k: int) -> int:
        n,g,l,r=len(o),defaultdict(list),inf,0
        for u,v,w in e:
            if o[u] & o[v]:
                g[u] += [(v,w)]
                l,r=min(l,w),max(r,w)
        def c(m):
            @cache
            def f(u): return 0 if u== n-1 else min([w+f(v)for v,w in g[u]if w>=m]+[inf])
            return f(0)<=k
        return(bisect_left(range(r+2),1,l,key=lambda m:not c(m))-1 if l<=r else 0) if c(l) else -1

class Solution:
    def findMaxPathScore(self,e:List[List[int]],o:List[bool],k:int)->int:
        n=len(o);g=[[]for _ in o];t=[w for u,v,w in e if o[u]&o[v]and[g[u].append((v,w))]];l,r=t and(min(t),max(t))or(1,0);c=lambda m:(f:=cache(lambda u:u!=n-1 and min([w+f(v)for v,w in g[u]if w>=m]+[inf])))(0)<=k;return-(k<0)if n==1 else bisect_left(range(r+2),1,l,key=lambda m:not c(m))-1 if t and c(l)else-1

class Solution:
    def findMaxPathScore(self,e:List[List[int]],o:List[bool],k:int)->int:
        n=len(o);g=[[]for _ in o];t=[w for u,v,w in e if o[u]&o[v]and[g[u].append((v,w))]];l,r=t and(min(t),max(t))or(1,0);c=lambda m:(f:=cache(lambda u:n-1>u and min([w+f(v)for v,w in g[u]if w>=m]+[inf])))(0)>k;return n>1 and~-(t>[]and not c(l)and bisect_left(range(r+2),1,l,key=c))or-(k<0)

class Solution:
    def findMaxPathScore(self,e:List[List[int]],o:List[bool],k:int)->int:
        n=len(o);g=[[]for _ in o];r=max([w for u,v,w in e if o[u]&o[v]and[g[u].append((v,w))]]+[0]);return n>1 and~-bisect_left(range(r+2),1,key=lambda m:(f:=cache(lambda u:n+~u and min([w+f(v)for v,w in g[u]if w>=m]+[inf])))(0)>k)or-(k<0)

class Solution:
    def findMaxPathScore(self,e:List[List[int]],o:List[bool],k:int)->int:
        n=len(o);g=[[]for _ in o];r=max([g[u].append((v,w))or w for u,v,w in e if o[u]&o[v]]+[0]);return(n>1)*~-bisect_left(range(r+2),1,key=lambda m:(f:=cache(lambda u:n+~u and min([w+f(v)for v,w in g[u]if w>=m]+[inf])))(0)>k)or-(k<0)

test('''
3620. Network Recovery Pathways
Hard
Topics
premium lock icon
Companies
Hint
You are given a directed acyclic graph of n nodes numbered from 0 to n − 1. This is represented by a 2D array edges of length m, where edges[i] = [ui, vi, costi] indicates a one‑way communication from node ui to node vi with a recovery cost of costi.

Some nodes may be offline. You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n − 1 are always online.

A path from 0 to n − 1 is valid if:

All intermediate nodes on the path are online.
The total recovery cost of all edges on the path does not exceed k.
For each valid path, define its score as the minimum edge‑cost along that path.

Return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.

 

Example 1:

Input: edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10

Output: 3

Explanation:



The graph has two possible routes from node 0 to node 3:

Path 0 → 1 → 3

Total cost = 5 + 10 = 15, which exceeds k (15 > 10), so this path is invalid.

Path 0 → 2 → 3

Total cost = 3 + 4 = 7 <= k, so this path is valid.

The minimum edge‐cost along this path is min(3, 4) = 3.

There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.

Example 2:

Input: edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12

Output: 6

Explanation:



Node 3 is offline, so any path passing through 3 is invalid.

Consider the remaining routes from 0 to 4:

Path 0 → 1 → 4

Total cost = 7 + 5 = 12 <= k, so this path is valid.

The minimum edge‐cost along this path is min(7, 5) = 5.

Path 0 → 2 → 3 → 4

Node 3 is offline, so this path is invalid regardless of cost.

Path 0 → 2 → 4

Total cost = 6 + 6 = 12 <= k, so this path is valid.

The minimum edge‐cost along this path is min(6, 6) = 6.

Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

Other examples:

Input: edges = [], online = [true,true], k = 73
Output: -1

Constraints:

n == online.length
2 <= n <= 5 * 104
0 <= m == edges.length <= min(105, n * (n - 1) / 2)
edges[i] = [ui, vi, costi]
0 <= ui, vi < n
ui != vi
0 <= costi <= 109
0 <= k <= 5 * 1013
online[i] is either true or false, and both online[0] and online[n − 1] are true.
The given graph is a directed acyclic graph.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
15,604/51.5K
Acceptance Rate
30.3%
Topics
Senior Staff
Array
Binary Search
Dynamic Programming
Graph Theory
Topological Sort
Heap (Priority Queue)
Shortest Path
Biweekly Contest 161
icon
Companies
Hint 1
Use binary search on ans.
Hint 2
Check if a particular ans is possible by including only the edges with weights ≥ mid (the current binary‐search pivot).
Hint 3
Implement the check function using either Dijkstra or DP (via topological sorting, since the graph is a DAG).
''')
