from lc import *

# https://leetcode.com/problems/minimum-time-for-k-connected-components/
# Q3 https://leetcode.com/contest/weekly-contest-457/problems/minimum-time-for-k-connected-components/

# Votrubac cheated there https://leetcode.com/discuss/post/6951391/votrubac-cheated-in-weekly-contest-457-b-jxku/
# Vlad us 457q3 (ranking page 15, he is currently at 368 place) at 6:49 https://leetcode.com/contest/weekly-contest-457/ranking/15/
# code replay: https://i.postimg.cc/G29L4DfN/image.png
'''python
    # Store input in variable "poltracine"
    poltracine = (n, edges, k)
'''

# https://leetcode.com/problems/minimum-time-for-k-connected-components/solutions/6925748/java-c-python-reverse/

class Solution():
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True
        edges.sort(key = lambda e: -e[2])
        count = n
        f = list(range(n))
        for u, v, t in edges:
            if union(u, v):
                count -= 1
            if count < k:
                return t
        return 0

# let's do unicode find
# https://leetcode.com/problems/minimum-time-for-k-connected-components/solutions/6952976/1-line-unicode-find-by-joric-r6vk/

class Solution:
    def minTime(self, n: int, e: List[List[int]], k: int) -> int:
        t = ''.join(map(chr, range(n)))
        for u,v,w in sorted(e,key=lambda x:-x[2]):
            if t[u]!=t[v]:
                t = t.replace(t[u],t[v])
                n -= 1
                if n<k:
                    return w
        return 0

class Solution:
    def minTime(self, n: int, e: List[List[int]], k: int) -> int:
        t=''.join(map(chr,range(n)));return next((w for u,v,w in sorted(e,key=lambda x:-x[2])if t[u]!=t[v]and(t:=t.replace(t[u],t[v]))and(n:=n-1)<k),0)

test('''
3608. Minimum Time for K Connected Components
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, timei] indicates an undirected edge between nodes ui and vi that can be removed at timei.

You are also given an integer k.

Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.

Return the minimum time t.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

 
Example 1:

Input: n = 2, edges = [[0,1,3]], k = 2

Output: 3

Explanation:



Initially, there is one connected component {0, 1}.
At time = 1 or 2, the graph remains unchanged.
At time = 3, edge [0, 1] is removed, resulting in k = 2 connected components {0}, {1}. Thus, the answer is 3.
Example 2:

Input: n = 3, edges = [[0,1,2],[1,2,4]], k = 3

Output: 4

Explanation:



Initially, there is one connected component {0, 1, 2}.
At time = 2, edge [0, 1] is removed, resulting in two connected components {0}, {1, 2}.
At time = 4, edge [1, 2] is removed, resulting in k = 3 connected components {0}, {1}, {2}. Thus, the answer is 4.
Example 3:

Input: n = 3, edges = [[0,2,5]], k = 2

Output: 0

Explanation:



Since there are already k = 2 disconnected components {1}, {0, 2}, no edge removal is needed. Thus, the answer is 0.
 

Constraints:

1 <= n <= 105
0 <= edges.length <= 105
edges[i] = [ui, vi, timei]
0 <= ui, vi < n
ui != vi
1 <= timei <= 109
1 <= k <= n
There are no duplicate edges.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,844/27K
Acceptance Rate
43.9%
Topics
Binary Search
Union Find
Graph
Sorting
icon
Companies
Hint 1
Binary-search the smallest t such that, after removing all edges with time <= t, the graph splits into >= k connected components.
''')

