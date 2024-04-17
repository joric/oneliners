from lc import *

def init(root: 'TreeNode', p: int, q: int):
    global g_p, g_q
    f = lambda r,x:r and(r if r.val==x else f(r.left,x)or f(r.right,x))
    g_p,g_q =[f(root,x) for x in (p,q)]

class Launcher:
    def lowestCommonAncestor(self, root: 'TreeNode', p: int, q: int) -> 'TreeNode':
        global g_p, g_q
        return Solution().lowestCommonAncestor(root, g_p, g_q)

def check(res, exp, *args):
    return res and exp and res.val==exp.val

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/5033857/one-line-solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

class Solution:
    def lowestCommonAncestor(self, n: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return(f:=lambda n:n and((l:=f(n.left),r:=f(n.right))[bool(r)],n)[bool(n in(p,q)or l and r)])(n)

test('''
236. Lowest Common Ancestor of a Binary Tree
Medium

16145

401

Add to List

Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
Accepted
1,596,382
Submissions
2,571,711
''')
