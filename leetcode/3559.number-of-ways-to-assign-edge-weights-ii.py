from lc import *

# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/?envType=daily-question&envId=2026-06-12

class Solution:
    def assignEdgeWeights(self, e: List[List[int]], q: List[List[int]]) -> List[int]:
        g=defaultdict(set)
        h=defaultdict(set)
        for u,v in e:
            g[u].add(v)
            g[v].add(u)
        for u,v in q:
            h[u].add(v)
            h[v].add(u)

        d,l,f={},{},{}

        def r(x):
            if x in f:
                f[x]=r(f[x])
                return f[x]
            return x

        def t(u,w):
            d[u]=w

            for v in g[u]:
                if v not in d:
                    t(v,w+1)
                    f[v] = u

            for v in h[u]:
                if v in d:
                    l[(u,v)]=r(v)
                    l[(v,u)]=r(v)
        t(1,0)
        return [(i:=d[x]+d[y]-2*d[l[x,y]])and pow(2,i-1,10**9+7)for x,y in q]

class Solution:
    def assignEdgeWeights(self,e:List[List[int]],q:List[List[int]])->List[int]:
        s,m=setitem,defaultdict;g,h,d,l,f=m(set),m(set),{},{},{}
        [a[u].add(v)or a[v].add(u)for a,b in((g,e),(h,q))for u,v in b]
        r=lambda x:s(f,x,r(f[x]))or f[x]if x in f else x
        t=lambda u,w:(s(d,u,w),[t(v,w+1)==s(f,v,u)for v in g[u]if(v in d)^1],[s(l,(u,v),r(v))or s(l,(v,u),r(v))for v in h[u]if v in d])
        t(1,0);return[(i:=d[x]+d[y]-2*d[l[x,y]])and pow(2,i-1,10**9+7)for x,y in q]

class Solution:
    def assignEdgeWeights(self,e:List[List[int]],q:List[List[int]])->List[int]:
        s,m=setitem,defaultdict;g,h,d,l,f=m(set),m(set),{},{},{};[a[u].add(v)or a[v].add(u)for a,b in((g,e),(h,q))for u,v in b];r=lambda x:s(f,x,r(f[x]))or f[x]if x in f else x;t=lambda u,w:(s(d,u,w),[t(v,w+1)==s(f,v,u)for v in g[u]if(v in d)^1],[s(l,(u,v),r(v))or s(l,(v,u),r(v))for v in h[u]if v in d]);t(1,0);return[(i:=d[x]+d[y]-2*d[l[x,y]])and pow(2,i-1,10**9+7)for x,y in q]

test('''
3559. Number of Ways to Assign Edge Weights II
Hard
Topics
premium lock icon
Companies
Hint
There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.

The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.

You are given a 2D integer array queries. For each queries[i] = [ui, vi], determine the number of ways to assign weights to edges in the path such that the cost of the path between ui and vi is odd.

Return an array answer, where answer[i] is the number of valid assignments for queries[i].

Since the answer may be large, apply modulo 109 + 7 to each answer[i].

Note: For each query, disregard all edges not in the path between node ui and vi.

 

Example 1:



Input: edges = [[1,2]], queries = [[1,1],[1,2]]

Output: [0,1]

Explanation:

Query [1,1]: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.
Query [1,2]: The path from Node 1 to Node 2 consists of one edge (1 → 2). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
Example 2:



Input: edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]

Output: [2,1,4]

Explanation:

Query [1,4]: The path from Node 1 to Node 4 consists of two edges (1 → 3 and 3 → 4). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.
Query [3,4]: The path from Node 3 to Node 4 consists of one edge (3 → 4). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
Query [2,5]: The path from Node 2 to Node 5 consists of three edges (2 → 1, 1 → 3, and 3 → 5). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.
 

Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i] == [ui, vi]
1 <= queries.length <= 105
queries[i] == [ui, vi]
1 <= ui, vi <= n
edges represents a valid tree.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
7,707/13K
Acceptance Rate
59.5%
Topics
Senior Staff
Array
Math
Dynamic Programming
Bit Manipulation
Tree
Depth-First Search
Biweekly Contest 157
icon
Companies
Hint 1
Dynamic programming with states chainLength and sumParity.
Hint 2
Use Lowest Common Ancestor to find the distance between any two nodes quickly in O(logn).
''')
