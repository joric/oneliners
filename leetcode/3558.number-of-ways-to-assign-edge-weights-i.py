from lc import *

# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/solutions/6777062/python-dp-dfs-cache-by-pbelskiy-mb7i/?envType=daily-question&envId=2026-06-11

class Solution:
    def assignEdgeWeights(self, e: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in e:
            g[a].append(b)
            g[b].append(a)

        @cache
        def f(a, p, o, t):
            if a == t:
                return 1 if o else 0
            m = 0
            for b in g[a]:
                if b == p: continue
                m += f(b, a, not o, t)
                m += f(b, a, o, t)
            return m % (10**9 + 7)

        def l(a, p, d):
            if len(g[a]) == 1 and next(iter(g[a])) == p:
                s[a] = d
                return d
            return max(l(b, a, d + 1) for b in g[a] if b != p)

        s = {}
        m = l(1, 0, 0)
        for x, y in s.items():
            if y == m:
                r = f(1, 0, False, x)
                f.cache_clear()
                return r
        return 0


class Solution:
    def assignEdgeWeights(self, e: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in e:
            g[a].append(b)
            g[b].append(a)

        f=cache(lambda a,p,o,t:(1 if o else 0)if a==t else sum(f(b,a,not o,t)+f(b,a,o,t)for b in g[a]if b!=p)%(10**9+7))

        def l(a, p, d):
            if len(g[a]) == 1 and next(iter(g[a])) == p:
                s[a] = d
                return d
            return max(l(b,a,d+1)for b in g[a]if b!=p)

        s = {}
        m = l(1,0,0)
        for x,y in s.items():
            if y == m:
                r = f(1, 0, False, x)
                f.cache_clear()
                return r
        return 0

class Solution:
    def assignEdgeWeights(self, e: List[List[int]]) -> int:
        g=defaultdict(list);[(g[a].append(b),g[b].append(a))for a,b in e];s={};f=cache(lambda a,p,o,t:(o if a==t else sum(f(b,a,o^1,t)+f(b,a,o,t)for b in g[a]if b-p))%(10**9+7));l=lambda a,p,d:(setitem(s,a,d),d)[1]if len(g[a])==1and g[a][0]==p else max(l(b,a,d+1)for b in g[a]if b-p);m=l(1,0,0);return next((f(1,0,0,x)for x,y in s.items()if y==m),0)

class Solution:
    def assignEdgeWeights(self, e: List[List[int]]) -> int:
        g=defaultdict(list);[g[a].append(b)or g[b].append(a)for a,b in e];l=lambda a,p,d:(d,a)if g[a]==[p]else max(l(b,a,d+1)for b in g[a]if b-p);t=l(1,0,0)[1];f=cache(lambda a,p,o:(o if a==t else sum(f(b,a,o^1)+f(b,a,o)for b in g[a]if b-p))%(10**9+7));return f(1,0,0)

test('''
3558. Number of Ways to Assign Edge Weights I
Medium
Topics
premium lock icon
Companies
Hint
There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.

The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.

Select any one node x at the maximum depth. Return the number of ways to assign edge weights in the path from node 1 to x such that its total cost is odd.

Since the answer may be large, return it modulo 109 + 7.

Note: Ignore all edges not in the path from node 1 to x.

 

Example 1:



Input: edges = [[1,2]]

Output: 1

Explanation:

The path from Node 1 to Node 2 consists of one edge (1 → 2).
Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
Example 2:



Input: edges = [[1,2],[1,3],[3,4],[3,5]]

Output: 2

Explanation:

The maximum depth is 2, with nodes 4 and 5 at the same depth. Either node can be selected for processing.
For example, the path from Node 1 to Node 4 consists of two edges (1 → 3 and 3 → 4).
Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.
 

Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i] == [ui, vi]
1 <= ui, vi <= n
edges represents a valid tree.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
14,074/26.4K
Acceptance Rate
53.4%
Topics
Staff
Math
Tree
Depth-First Search
Biweekly Contest 157
icon
Companies
Hint 1
Depth‑First Search (DFS) to compute the depth of each node from the root.
Hint 2
Find the maximum depth, max_depth.
Hint 3
The number of 2s doesn’t affect parity; we only need an odd number of 1s along the path.
Hint 4
The number of ways to choose an odd count of 1s among max_depth edges is 2^(max_depth-1).
''')
