from lc import *

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def f(x):
            if not x:
                return 0
            l = f(x.left)
            r = f(x.right)
            if l==None or r==None or abs(l-r)>1:
                return None
            return 1+max(l,r)
        return f(root) if root else True

class Solution:
    def isBalanced(self, root: TreeNode):
        return not root or abs((f:=lambda r:1+max(f(r.left),f(r.right)) if r else 0)(root.left)-f(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return not root or (f:=lambda x:(None if (l:=f(x.left))==None or (r:=f(x.right))==None or abs(l-r)>1 else 1+max(l,r)) if x else 0)(root)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return (f:=lambda x:(((l:=f(x.left))<0 or (r:=f(x.right))<0 or abs(l-r)>1) and -1) or 1+max(l,r) if x else 0)(root)>=0

# POTD 2026-02-08

class Solution:
    def isBalanced(self, t: TreeNode) -> bool:
        return(f:=lambda x:x and((l:=f(x.left))>=0<=(r:=f(x.right))and 2>abs(l-r)and 1+max(l,r)or-1)or 0)(t)>=0

test('''
110. Balanced Binary Tree
Easy

7631

402

Add to List

Share
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Example 4:

Input: root = [3,9,20,null,null,15,7]
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
''')