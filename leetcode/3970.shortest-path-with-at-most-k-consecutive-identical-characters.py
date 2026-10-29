from lc import * 

# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/solutions/8349354/always-be-wise-and-think-twise-to-solve-4v1rg/?envType=daily-question&envId=2026-10-30

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
        pq=[(0,0,1)]
        dist={(0,1):0}
        while pq:
            cost,node,run=heappop(pq)
            if cost!=dist.get((node,run),inf):
                continue
            if node==n-1:
                return cost
            for v,weight in graph[node]:
                if labels[v]==labels[node]:
                    run1=run+1
                else:
                    run1=1
                if run1>k:
                    continue
                cost1=cost+weight
                stage1=(v,run1)
                if cost1<dist.get(stage1,inf):
                    dist[stage1]=cost1
                    heappush(pq,(cost1,v,run1))
        return -1

class Solution:
    def shortestPath(self, n: int, e: List[List[int]], l: str, k: int):
        p=[(0,0,1)];g=defaultdict(list);[g[u].append((v,w,l[u]==l[v]))for u,v,w in e];return next((c for c,u,r in iter(lambda:p and heappop(p),p)if u>n-2or(u,r)not in g and(g[u,r]or any(heappush(p,(c+w,v,r*f+1))for v,w,f in g[u]if r*f<k))),-1)

test('''
3970. Shortest Path With At Most K Consecutive Identical Characters
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

 

Example 1:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

Output: 3

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.
Example 2:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

Output: 2

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.
Example 3:

Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

Output: -1

Explanation:

There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.

 

Constraints:

1 <= n == labels.length <= 5 * 104
0 <= edges.length <= 5 * 104
edges[i] == [ui, vi, wi]
0 <= ui, vi <= n - 1
ui != vi
1 <= wi <= 104
labels consists of lowercase English letters
1 <= k <= 50
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
19,564/44.1K
Acceptance Rate
44.3%
Topics
Staff
String
Graph Theory
Heap (Priority Queue)
Shortest Path
Weekly Contest 507
icon
Companies
Hint 1
The validity of a path depends not only on the current node, but also on how many consecutive times the current node’s label has appeared at the end of the path.
Hint 2
Use Dijkstra on states (node, count), where count is the current consecutive run length of labels[node].
Hint 3
When moving from node u to node v, the next count becomes count + 1 if labels[u] == labels[v], otherwise it becomes 1. Ignore transitions where the next count exceeds k.
Hint 4
''')
