from lc import *

# https://leetcode.com/problems/find-eventual-safe-states/discuss/128872/Python-easy-peasy-11-lines-very-simple-and-clear-solution-192-ms-beats-100/641697

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        v,s=set(),set()
        def f(u):
            if u in p:
                return u in s
            v.add(u)
            if all(map(f,g[u])):
                s.add(u)
                return True
        return filter(f,range(len(g)))

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        v,s=set(),set();return filter(f:=lambda u:u in s if u in v else v.add(u)or all(map(f,g[u]))and[s.add(u)],range(len(g)))

# https://leetcode.com/problems/find-eventual-safe-states/solutions/4071045/shortest-7-line-dfs/?envType=daily-question&envId=2025-01-24

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        v = set()
        @cache
        def f(i):
            if i in v:
                return False
            v.add(i)
            if not g[i] or all(f(j) for j in g[i]):
                return True
        return [i for i in range(len(g))if f(i)]

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        v=set();return[*filter(f:=cache(lambda i:not v&{i}and(v.add(i)or all(map(f,g[i])))),range(len(g)))]

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        v={-1};return[*filter(f:=cache(lambda i:not v&{i}and(v.add(i)or all(map(f,g[i])))),range(len(g)))]

test('''
802. Find Eventual Safe States
Medium

4124

372

Add to List

Share
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

Other examples:

Input: graph = [[],[0,2,3,4],[3],[4],[]]
Output: [0,1,2,3,4]

Constraints:

n == graph.length
1 <= n <= 10^4
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 10^4].
''')
