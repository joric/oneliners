from lc import *

# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/solutions/334577/java-c-python-two-recursive-solution/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]

class Solution:
    def lcaDeepestLeaves(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(r):
            if not r: return 0,None
            (a,c),(b,d)=map(f,(r.left,r.right))
            return a>b and (a+1,c)or(a<b and(b+1,d))or(a+1,r)
        return f(r)[1]

# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/submissions/426560682/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.lca, self.deepest = None, 0
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)
        helper(root, 0)
        return self.lca

class Solution:
    def lcaDeepestLeaves(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        p=[None,0];(f:=lambda t,d:setitem(p,1,max(p[1],d))or(((l:=f(t.left,d+1))==(r:=f(t.right,d+1))==p[1]and setitem(p,0,t)or max(l,r))if t else d))(r,0);return p[0]

test('''
1123. Lowest Common Ancestor of Deepest Leaves
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
 

Constraints:

The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 1000
The values of the nodes in the tree are unique.
 

Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Seen this question in a real interview before?
1/5
Yes
No
Accepted
124K
Submissions
169.8K
Acceptance Rate
73.1%
Topics
Hash Table
Tree
Depth-First Search
Breadth-First Search
Binary Tree
Companies
Hint 1
Do a postorder traversal.
Hint 2
Then, if both subtrees contain a deepest leaf, you can mark this node as the answer (so far).
Hint 3
The final node marked will be the correct answer.
Similar Questions
Lowest Common Ancestor of a Binary Tree IV
Medium
''')
