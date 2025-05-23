from lc import *

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        p = [*range(n)]
        r = [1] * n
        def f(i):
            while i!=p[i]:
                p[i]=i=p[p[i]]
            return i
        def u(i,j):
            i,j = f(i),f(j)
            if i==j:
                return 0
            c = r[i]*r[j]
            if r[i]>=r[j]:
                p[j]=i
                r[i]+=r[j]
            else:
                p[i]=j
                r[j]+=r[i]
            return c
        return n*(n-1)//2 - sum(u(i,j) for i,j in edges)

class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        g,s,r = defaultdict(set),set(),0
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
        def f(i):
            if i not in s:
                s.add(i)
                return 1+sum(f(j) for j in g[i] if j not in s)
            return 0
        for i in range(n):
            c = f(i)
            n -= c
            r += c * n
        return r

class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        return (g:=defaultdict(set),s:=set(),any(g[a].add(b) or g[b].add(a) for a,b in edges)) and sum((c:=(f:=lambda i:i not in s and (s.add(i) or 1+sum(f(j) for j in g[i] if j not in s)))(i))*(n:=n-c) for i in range(n))

test('''
2316. Count Unreachable Pairs of Nodes in an Undirected Graph
Medium

577

17

Add to List

Share
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

 

Example 1:

Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

Example 2:

Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.

Example 3:

Input: n = 6, edges = [[0,1],[2,3],[4,5]]
Output: 12

Constraints:

1 <= n <= 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.

Accepted
21,830
Submissions
56,194
''')