from lc import *

# Q3. https://leetcode.com/contest/biweekly-contest-128/
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

class Solution:
    def minimumTime(self, n: int, e: List[List[int]], d: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u,v,w in e:
            g[u].append((v,w))
            g[v].append((u,w))
        h = [(0,0)]
        r = [-1]*n
        while h:
            t,i = heappop(h)
            if r[i]!=-1 or t>=d[i]:
                continue
            r[i]=t
            for j,w in g[i]:
                heappush(h,(t+w,j))
        return r

class Solution:
    def minimumTime(self, n: int, e: List[List[int]], d: List[int]) -> List[int]:
        g,h,r,p=defaultdict(list),[(0,0)],[-1]*n,heappop;[g[v].append((u,w))or g[u].append((v,w))for u,v,w in e];f=lambda t,i:(-1==r[i]and t<d[i]and(setitem(r,i,t),[heappush(h,(t+w,j))for j,w in g[i]]),h and f(*p(h)));return f(*p(h))and r

test('''
3112. Minimum Time to Visit Disappearing Nodes
Medium

13

3

Add to List

Share
There is an undirected graph of n nodes. You are given a 2D array edges, where edges[i] = [ui, vi, lengthi] describes an edge between node ui and node vi with a traversal time of lengthi units.

Additionally, you are given an array disappear, where disappear[i] denotes the time when the node i disappears from the graph and you won't be able to visit it.

Notice that the graph might be disconnected and might contain multiple edges.

Return the array answer, with answer[i] denoting the minimum units of time required to reach node i from node 0. If node i is unreachable from node 0 then answer[i] is -1.

 

Example 1:



Input:  n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]

Output:  [0,-1,4]

Explanation:

We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears.

For node 0, we don't need any time as it is our starting point.
For node 1, we need at least 2 units of time to traverse edges[0]. Unfortunately, it disappears at that moment, so we won't be able to visit it.
For node 2, we need at least 4 units of time to traverse edges[2].
Example 2:



Input:  n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]

Output:  [0,2,3]

Explanation:

We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears.

For node 0, we don't need any time as it is the starting point.
For node 1, we need at least 2 units of time to traverse edges[0].
For node 2, we need at least 3 units of time to traverse edges[0] and edges[1].
Example 3:

Input: n = 2, edges = [[0,1,1]], disappear = [1,1]

Output: [0,-1]

Explanation:

Exactly when we reach node 1, it disappears.

 

Constraints:

1 <= n <= 5 * 104
0 <= edges.length <= 105
edges[i] == [ui, vi, lengthi]
0 <= ui, vi <= n - 1
1 <= lengthi <= 105
disappear.length == n
1 <= disappear[i] <= 105
Accepted
6,408
Submissions
24,167
''')
