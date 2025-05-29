from lc import *

# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/solutions/6101069/easy-python-solution-bipartite-graph/?envType=daily-question&envId=2025-05-29

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)

        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
            
        vis = set()

        # Function to colour every adjacent node differently
        def bipartite(n, graph):
            red = set()
            blue = set()
            q = deque()
            q.append((True, n))
            visited = set()
            visited.add(n)
            while q:
                c, node = q.popleft()
                if c: red.add(node)
                else: blue.add(node)
                for nei in graph[node]:
                    if nei in visited: continue
                    visited.add(nei)
                    q.append((not c, nei))
            return red, blue

        red1, blue1 = bipartite(edges1[0][0], tree1)
        red2, blue2 = bipartite(edges2[0][0], tree2)
        
        ans = []
        maxi = max(len(red2), len(blue2))

        print(len(red1),len(blue1))

        for i in sorted(tree1.keys()):
            if i in red1:
                ans.append(len(red1) + maxi)
            else:
                ans.append(len(blue1) + maxi)
        return ans

# TODO: maybe use 785.is-graph-bipartite.py
class Solution:
    def maxTargetNodes(self, a: List[List[int]], b: List[List[int]]) -> List[int]:
        t=lambda e:(g:=defaultdict(list),[g[u].append(v)or g[v].append(u)for u,v in e])[0]
        def f(n,g):
            r,b,s,q = set(),set(),set(),deque()
            q.append((True, n))
            s.add(n)
            while q:
                c, u = q.popleft()
                if c: r.add(u)
                else: b.add(u)
                for v in g[u]:
                    if v in s: continue
                    s.add(v)
                    q.append((not c, v))
            return r,b
        ((a,b),u),((c,d),v)=[(f(e[0][0],g:=t(e)),g)for e in (a,b)]
        return[max(len(c),len(d))+(len(b),len(a))[i in a]for i in sorted(u.keys())]

test('''
3373. Maximize the Number of Target Nodes After Connecting Trees II
Hard
Topics
premium lock icon
Companies
Hint
There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

Output: [8,7,7,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 4 from the second tree.
For i = 2, connect node 2 from the first tree to node 7 from the second tree.
For i = 3, connect node 3 from the first tree to node 0 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]

Output: [3,6,6,6,6]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
8,056/14.1K
Acceptance Rate
57.3%
Topics
Tree
Depth-First Search
Breadth-First Search
icon
Companies
Hint 1
Compute an array even where even[u] is the number of nodes at an even distance from node u, for every u of the first tree.
Hint 2
Compute an array odd where odd[u] is the number of nodes at an odd distance from node u, for every u of the second tree.
Hint 3
answer[i] = even[i]+ max(odd[1], odd[2], …, odd[m - 1])
Similar Questions
Find Minimum Diameter After Merging Two Trees
Hard
''')
