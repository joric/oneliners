from lc import *

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        s = set()
        t = [inf]*n
        def f(i,r):
            if i in s or edges[i]==-1:
                return -1
            if t[i]<r:
                return r-t[i]
            t[i] = r
            x = f(edges[i],r+1)
            s.add(i)
            return x
        return max(f(i,0) for i in range(n))

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        return (n:=len(edges),s:=set(),t:=[inf]*n) and max((f:=lambda i,r:-1 if i in s or edges[i]==-1 else r-t[i] if t[i]<r else (setitem(t,i,r),x:=f(edges[i],r+1),s.add(i),x)[-1])(i,0) for i in range(n))

test('''
2360. Longest Cycle in a Graph
Hard

756

12

Add to List

Share
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

 

Example 1:


Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Example 2:


Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
 

Constraints:

n == edges.length
2 <= n <= 10^5
-1 <= edges[i] < n
edges[i] != i
Accepted
18,731
Submissions
47,312
''')
