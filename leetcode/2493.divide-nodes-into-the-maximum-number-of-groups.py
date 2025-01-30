from lc import *

# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/solutions/3998941/very-short-just-bfs/?envType=daily-question&envId=2025-01-30
# TODO

class Solution:
    def magnificentSets(self, n: int, e: List[List[int]]) -> int:
        g = defaultdict(set)
        r = defaultdict(lambda:-inf)
        for u,v in e:
            u,v = u-1, v-1
            g[u].add(v)
            g[v].add(u)
        for u in range(n):
            q, s, t = [u], set([u]), 0
            while q:
                t += 1
                p = set()
                for u in q:
                    for v in g[u]:
                        if v in q:
                            return -1
                        if v not in s:
                            p.add(v)
                            s.add(v)
                q = p
            k = min(s)
            r[k] = max(r[k], t)
        return sum(r.values())

test('''
2493. Divide Nodes Into the Maximum Number of Groups
Solved
Hard
Topics
Companies
Hint
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.
 

Constraints:

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
13.5K
Submissions
29.9K
Acceptance Rate
45.1%
Topics
Breadth-First Search
Union Find
Graph
Companies
Hint 1
If the graph is not bipartite, it is not possible to group the nodes.
Hint 2
Notice that we can solve the problem for each connected component independently, and the final answer will be just the sum of the maximum number of groups in each component.
Hint 3
Finally, to solve the problem for each connected component, we can notice that if for some node v we fix its position to be in the leftmost group, then we can also evaluate the position of every other node. That position is the depth of the node in a bfs tree after rooting at node v.
''')
