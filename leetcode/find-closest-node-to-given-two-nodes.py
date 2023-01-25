from lc import *

# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/discuss/3096734/Python-or-DFS

class Solution:
    def closestMeetingNode(self, e: List[int], a: int, b: int) -> int:
        v,w,r = set(),set(),set()
        while a!=-1 or b!=-1:
            a!=-1 and ((a in w) or a==b) and r.add(a)
            b!=-1 and ((b in v) or a==b) and r.add(b)
            if r:
                return min(r)
            a!=-1 and a not in v and (v.add(a),a:=e[a]) or (a:=-1)
            b!=-1 and b not in w and (w.add(b),b:=e[b]) or (b:=-1)
        return -1

class Solution:
    def closestMeetingNode(self, e: List[int], a: int, b: int) -> int:
        return (v:=set(),w:=set(),r:=set()) and next((min(r) if r else -1 for _ in count() if (a==-1 and b==-1) or not (a!=-1 and ((a in w) or a==b) and r.add(a),b!=-1 and ((b in v) or a==b) and r.add(b)) or r or not (a!=-1 and a not in v and (v.add(a),a:=e[a]) or (a:=-1),b!=-1 and b not in w and (w.add(b),b:=e[b]) or (b:=-1))),-1)

test('''

2359. Find Closest Node to Given Two Nodes
Medium

777

180

Add to List

Share
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.


Example 1:

Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2

Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.


Example 2:

Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2

Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.


Example 3:
Input: edges = [5,4,5,4,3,6,-1], node1 = 0, node2 = 1
Output: -1


Example 4:
Input: edges = [5,-1,3,4,5,6,-1,-1,4,3], node1 = 0, node2 = 0
Output: 0

Constraints:

n == edges.length
2 <= n <= 10^5
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n

''')


