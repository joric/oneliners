from lc import *

class Solution1:
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

class Solution(object):
    def isBalanced(self, root: TreeNode):
        return not root or abs((f:=lambda r:1+max(f(r.left),f(r.right)) if r else 0)(root.left)-f(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

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
