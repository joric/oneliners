from lc import *

# Q4. https://leetcode.com/contest/weekly-contest-392
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph

# unicode find (doesn't work)

class Solution:
    def minimumCost(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[int]:
        t,c,r=''.join(map(chr,range(n))),{},[]
        for u,v,w in e:
            t = t.replace(t[u],t[v])
            if u not in c:
                c[u] = w
            c[u] &= w
        return [0 if u==v else c[u]if t[u]==t[v]else -1 for u,v in q]

# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/discuss/4988824/Python-(Simple-Union-Find)

class Solution:
    def minimumCost(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[int]:
        d,c,r = {},[-1]*n,[]
        def f(u):
            if u in d:
                if d[u]!=u:
                    d[u] = f(d[u])
                return d[u]
            return u
        for u,v,w in e:
            x,y = f(u),f(v)
            c[y] = c[y]&w
            if x != y:
                c[y] = c[y]&c[x]
                d[x] = y
        return [0 if u==v else c[f(u)]if f(u)==f(v)else-1 for u,v in q]

class Solution:
    def minimumCost(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[int]:
        d,c,r={},[-1]*n,[];f=lambda u:u!=d[u]and setitem(d,u,f(d[u]))or d[u]if u in d else u;[(setitem(c,y:=f(v),c[y]&w),(x:=f(u))!=y and(setitem(c,y,c[y]&c[x]),setitem(d,x,y)))for u,v,w in e];return[0 if u==v else c[f(u)]if f(u)==f(v)else-1 for u,v in q]

test('''
3108. Minimum Cost Walk in Weighted Graph
Hard

0

0

Add to List

Share
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:


To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:

Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

Output: [0]

Explanation:


To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

 

Constraints:

1 <= n <= 105
0 <= edges.length <= 105
edges[i].length == 3
0 <= ui, vi <= n - 1
ui != vi
0 <= wi <= 105
1 <= query.length <= 105
query[i].length == 2
0 <= si, ti <= n - 1
Accepted
1,827
Submissions
7,812
''')
