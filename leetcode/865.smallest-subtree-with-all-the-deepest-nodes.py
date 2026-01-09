from lc import *

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solutions/410854/python-3-6-lines-bfs-lca-by-l1ne-za9o/?envType=daily-question&envId=2026-01-09

class Solution:
  def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:    
    last_q, q, parents = [], [root], {}
    while q:
      for node in q: parents[node.left] = parents[node.right] = node
      last_q, q = q, [node.left for node in q if node.left] + [node.right for node in q if node.right]
    while len(last_q) > 1: last_q = {parents[node] for node in last_q}
    return next(iter(last_q))

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solutions/6612886/two-lines-by-charnavoki-h68i/?envType=daily-question&envId=2026-01-09
# const subtreeWithAllDeepest = f = (n, x = d(n.right), y = d(n.left)) => x === y ? n : f(x > y ? n.right : n.left); const d = (n) => n ? 1 + Math.max(d(n.left), d(n.right)) : 0;

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        d=lambda n:1+max(d(n.left),d(n.right))if n else 0;return(f:=lambda n:(lambda x,y:n if x==y else f(n.right if x>y else n.left))(d(n.right),d(n.left))if n else None)(t)

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        d=lambda n:n and 1+max(d(n.left),d(n.right))or 0;return(f:=lambda n:n and(lambda x,y:n if x==y else f(n.right if x>y else n.left))(d(n.right),d(n.left)))(t)

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        d=lambda n:n and 1+max(d(n.left),d(n.right))or 0;return(f:=lambda n:n and(n if(x:=d(n.right))==(y:=d(n.left))else f(n.right if x>y else n.left)))(t)

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        d=lambda t:t and-~max(d(t.left),d(t.right))or 0;return(f:=lambda t:t and(t if(x:=d(t.right))==(y:=d(t.left))else f((t.left,t.right)[x>y])))(t)

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        d=lambda t:t and-~max(d(t.left),d(t.right))or 0;return(f:=lambda t:t and(t if(l:=d(t.left))==(r:=d(t.right))else f((t.left,t.right)[r>l])))(t)

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return 0, None
            l, r = dfs(root.left), dfs(root.right)
            if l[0] > r[0]: return l[0] + 1, l[1]
            elif l[0] < r[0]: return r[0] + 1, r[1]
            else: return l[0] + 1, root
        return dfs(root)[1]

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        def f(t):
            if not t: return 0, None
            (l:=f(t.left),r:=f(t.right))
            return(l[0]+1,l[1])if l[0]>r[0]else(r[0]+1,r[1])if(l[0]<r[0])else(l[0]+1,t)
        return f(t)[1]

class Solution:
    def subtreeWithAllDeepest(self, t: TreeNode) -> TreeNode:
        return(f:=lambda t:t and((((l:=f(t.left))[0]+1,t),((r:=f(t.right))[0]+1,r[1]))[l[0]<r[0]],(l[0]+1,l[1]))[l[0]>r[0]]or(0,0))(t)[1]

test('''
865. Smallest Subtree with all the Deepest Nodes
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

Other examples:

Input: root = [0,2,1,null,null,3]
Output: [3]

Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
 

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
171,785/235.8K
Acceptance Rate
72.9%
Topics
Hash Table
Tree
Depth-First Search
Breadth-First Search
Binary Tree
''')
