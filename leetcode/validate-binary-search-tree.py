from lc import *

# inorder/prev
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        p = None
        def f(r):
            nonlocal p
            if not r:
                return True
            if not f(r.left):
                return False
            if p and p.val >= r.val:
                return False
            p = r
            return f(r.right)
        return f(root)

# left/right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(r,a,b):
            if not r:
                return True
            if (a and a.val>=r.val) or (b and b.val<=r.val):
                return False
            return f(r.left,a,r) and f(r.right,r,b)
        return f(root,None,None)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return (f:=lambda r,a,b:not r or (not ((a and a.val>=r.val) or (b and b.val<=r.val))) and f(r.left,a,r) and f(r.right,r,b))(root,0,0)

# min/max
class Solution:
    def isValidBST(self, p: Optional[TreeNode], min=-inf, max=inf) -> bool:
        return (not p or (p.val>min and p.val<max) and self.isValidBST(p.left, min, p.val) and self.isValidBST(p.right, p.val, max))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return (f:=lambda p,a,b: not p or p.val>a and p.val<b and f(p.left,a,p.val) and f(p.right,p.val,b))(root,-inf,inf)


test('''
98. Validate Binary Search Tree
Medium

12920

1039

Add to List

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Custom:

Input: root = [1,1]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
''')
