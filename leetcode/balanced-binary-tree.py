from lc import *

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return 0
            left  = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return dfs(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode):
        return not root or abs((f:=lambda r:1+max(f(r.left),f(r.right)) if r else 0)(root.left)-f(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return (f:=lambda x:(l:=f(x.left),r:=f(x.right)) and ((l==-1 or r==-1 or abs(l-r)>1) and -1) or 1+max(l,r) if x else 0)(root)!=-1


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
    def isBalanced(self, root: TreeNode) -> bool:
        return not root or (f:=lambda x:not ((l:=f(x.left))==None or (r:=f(x.right))==None or abs(l-r)>1) and 1 + max(l,r) if x else 0)(root)

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
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
''')
