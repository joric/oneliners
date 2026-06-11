from lc import *

# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/solutions/8327610/four-simple-lines-of-code-by-mikposp-hpa3/

class Solution:
    def assignEdgeWeights(self, e: List[List[int]]) -> int:
        g = defaultdict(list)
        for v,u in map(sorted,e): g[v].append(u)
        f = lambda n,p:max([f(q,n)+1 for q in g[n] if q!=p]+[0])
        return pow(2,f(1,0)-1,10**9+7)

class Solution:
    def assignEdgeWeights(self, e: List[List[int]]) -> int:
        g=defaultdict(list);[g[v].append(u)for v,u in map(sorted,e)];f=lambda x,y:max([0]+[1+f(i,x)for i in g[x]if i-y]);return pow(2,f(1,0)-1,10**9+7)

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
