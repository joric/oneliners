from lc import *

# https://leetcode.com/problems/add-one-row-to-tree

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int, isLeft: bool = True) -> TreeNode:
        if d == 1:
            return TreeNode(v, root if isLeft else None, root if not isLeft else None)
        if not root:
            return None
        root.left = self.addOneRow(root.left, v, d - 1, True)
        root.right = self.addOneRow(root.right, v, d - 1, False)
        return root

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int, isLeft: bool = True) -> TreeNode:
        return TreeNode(v, root if isLeft else None, root if not isLeft else None) if d==1 else setattr(root,'left', self.addOneRow(root.left, v, d - 1, True)) or setattr(root,'right', self.addOneRow(root.right, v, d - 1, False)) or root if root else None

# updated 2024-04-16

class Solution:
    def addOneRow(self, r: TreeNode, v: int, d: int) -> TreeNode:
        return(f:=lambda r,d,l=1:TreeNode(v,r if l else None, r if not l else None)if d==1 else setattr(r,'left',f(r.left,d-1))or setattr(r,'right',f(r.right,d-1,0))or r if r else None)(r,d)

class Solution:
    def addOneRow(self, r: TreeNode, v: int, d: int) -> TreeNode:
        return(f:=lambda r,d,l=None:d==1 and TreeNode(v,l and r,(None,r)[not l])or r and(setattr(r,'left',f(r.left,d-1,1))or setattr(r,'right',f(r.right,d-1))or r))(r,d,1)

# https://leetcode.com/problems/add-one-row-to-tree/discuss/2666027/Python-3-one-line

class Solution:
    def addOneRow(self, r, v, d, s=1):
        return r and TreeNode(r.val, *(self.addOneRow(x, v, d-1, s) for x,s in ((r.left, 1), (r.right, -1)))) if d > 1 else TreeNode(v, *(r, None)[::s])

class Solution:
    def addOneRow(self, r: TreeNode, v: int, d: int) -> TreeNode:
        t=TreeNode;return(f:=lambda r,d,s:r and t(r.val,*(f(x,d-1,s)for x,s in((r.left,1),(r.right,-1))))if d>1 else t(v,*(r,None)[::s]))(r,d,1)

class Solution:
    def addOneRow(self, r: TreeNode, v: int, d: int) -> TreeNode:
        c=type(r);return(f:=lambda r,d,s=1:r and c(r.val,f(r.left,d-1),f(r.right,d-1,-1))if d>1 else c(v,*(r,None)[::s]))(r,d)

class Solution:
    def addOneRow(self, r: TreeNode, v: int, d: int) -> TreeNode:
        c=type(r);return(f:=lambda r,d,s=1:(r and c(r.val,f(r.left,d-1),f(r.right,d-1,-1)),c(v,*(r,None)[::s]))[d<2])(r,d)

test('''

623. Add One Row to Tree
Medium

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]

Other examples:

Input: root = [4,2,6,3,1,5], val = 1, depth = 1
Output: [1,4,null,2,6,3,1,5]

Input: root = [1,2,3,4], val = 5, depth = 1
Output: [5,1,null,2,3,4]

Input: root = [1,2,3,4], val = 5, depth = 4
Output: [1,2,3,4,null,null,null,5,5]

Constraints:

The number of nodes in the tree is in the range [1, 104].
The depth of the tree is in the range [1, 104].
-100 <= Node.val <= 100
-10^5 <= val <= 10^5
1 <= depth <= the depth of tree + 1

''')