from lc import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def serialize(self):
        nodes = {}
        def f(node):
            if node.val in nodes:
                return
            nodes[node.val] = node
            for nei in node.neighbors:
                f(nei)
        f(self)

        res = []
        k = 1
        while True:
            if k not in nodes:
                break
            res.append([])
            for node in nodes[k].neighbors:
                res[-1].append(node.val)
            k += 1
        return res

    def __repr__(self):
        return str(self.serialize())

    def parse(v):
        nodes = {}
        for i,nei in enumerate(v):
            k = i+1
            if k not in nodes:
                nodes[k] = Node(k)
            for i in nei:
                if i not in nodes:
                    nodes[i] = Node(i)
                nodes[k].neighbors.append(nodes[i])
        return None if 1 not in nodes else nodes[1]

def parser(hint, v):
    if 'Node' in hint and type(v) is list:
        return Node.parse(v)
    return v

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        v = {}
        def f(x):
            v[x] = Node(x.val)
            for n in x.neighbors:
                if n not in v:
                    f(n)
                v[x].neighbors.append(v[n])
            return v[x]
        return f(node) if node else None

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return (v:={}) or (f:=lambda x:(setitem(v,x,Node(x.val)),[(n not in v and f(n),v[x].neighbors.append(v[n])) for n in x.neighbors],v[x])[2])(node) if node else None

test('''
133. Clone Graph
Medium

7495

3085

Add to List

Share
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
Accepted
922,956
Submissions
1,775,431
Seen this question in a real interview before?

Yes

No
Copy List with Random Pointer
Medium
Clone Binary Tree With Random Pointer
Medium
Clone N-ary Tree
Medium
''', parser=parser)

