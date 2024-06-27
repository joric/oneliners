from lc import *

# https://leetcode.com/problems/find-center-of-star-graph/discuss/1108345/JavaC%2B%2BPython-Different-Ideas-1-line

class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return({*e[0]}&{*e[1]}).pop()

class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return e[0][e[0][1]in e[1]]

# https://leetcode.com/problems/find-center-of-star-graph/discuss/1108683/3-Python-Solutions/879073

class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return mode(e[0]+e[1])

test('''
1791. Find Center of Star Graph
Easy

1402

153

Add to List

Share
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
 

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
Accepted
193,571
Submissions
231,228
''')
