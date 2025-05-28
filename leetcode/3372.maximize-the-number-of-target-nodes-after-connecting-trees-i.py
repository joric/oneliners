from lc import *

# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/solutions/6099495/explained-simple-dfs-and-count-node-with-in-k-depth/?envType=daily-question&envId=2025-05-28

class Solution:
    def maxTargetNodes(self, a: List[List[int]], b: List[List[int]], k: int) -> List[int]:
        t=lambda e:(g:=defaultdict(list),[g[u].append(v) or g[v].append(u)for u,v in e])[0]
        f=lambda g,r,p,k,c=1:k>=0 and c+sum(f(g,u,r,k-1)for u in g[r]if u!=p)
        a,b=t(a),t(b)
        c=max(f(b,i,-1,k-1)for i in range(len(b)))
        return[c+f(a,i,-1,k)for i in range(len(a))]

class Solution:
    def maxTargetNodes(self, a: List[List[int]], b: List[List[int]], k: int) -> List[int]:
        t,f=lambda e:(g:=defaultdict(list),[g[u].append(v) or g[v].append(u)for u,v in e])[0],lambda g,r,p,k,c=1:k>=0 and c+sum(f(g,u,r,k-1)for u in g[r]if u!=p);a,b=t(a),t(b);c=max(f(b,i,-1,k-1)for i in range(len(b)));return[c+f(a,i,-1,k)for i in range(len(a))]

test('''
3372. Maximize the Number of Target Nodes After Connecting Trees I
Medium
Topics
premium lock icon
Companies
Hint
There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

Output: [9,7,9,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 0 from the second tree.
For i = 2, connect node 2 from the first tree to node 4 from the second tree.
For i = 3, connect node 3 from the first tree to node 4 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

Output: [6,3,3,3,3]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 1000
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
0 <= k <= 1000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,421/22.4K
Acceptance Rate
51.0%
Topics
Tree
Depth-First Search
Breadth-First Search
icon
Companies
Hint 1
For each node u in the first tree, find the number of nodes at a distance of at most k from node u.
Hint 2
For each node v in the second tree, find the number of nodes at a distance of at most k - 1 from node v.
Similar Questions
Find Minimum Diameter After Merging Two Trees
Hard
''')
