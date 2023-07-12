from lc import *

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143729/Python-DFS-and-BFS

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        def f(p,n):
            if p and n:
                g[p.val].append(n.val)
                g[n.val].append(p.val)
            if n.left:
                f(n, n.left)
            if n.right:
                f(n, n.right)
        f(None, root)
        q = [target.val]
        v = set(q)
        for i in range(k):
            p = []
            for i in q:
                for j in g[i]:
                    if j not in v:
                        p.append(j)
            q = p
            v |= set(q)
        return q

class Solution:
    def distanceK(self, r: TreeNode, t: TreeNode, k: int) -> List[int]:
        g,q = defaultdict(list),[t.val]
        v = set(q)
        f = lambda p,n:(p and(g[p.val].append(n.val),g[n.val].append(p.val)),n.left and f(n,n.left),n.right and f(n,n.right))
        f(None,r)
        for i in range(k):
            q = [j for i in q for j in g[i] if j not in v]
            v |= set(q)
        return q

class Solution:
    def distanceK(self, r: TreeNode, t: TreeNode, k: int) -> List[int]:
        g,q=defaultdict(list),[t.val];v=set(q);(f:=lambda p,n:(p and[g[x.val].append(y.val)for x,y in((p,n),(n,p))],[f(n,x)for x in(n.left,n.right)if x]))(None,r);[v:=v|set(q:=[j for i in q for j in g[i]if j not in v])for i in range(k)];return q

test('''
863. All Nodes Distance K in Binary Tree
Medium

8787

172

Add to List

Share
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
''',check=lambda res, expected, *args: set(res)==set(expected))

