from lc import *

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, s = [], []
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                res.append(root.val)
                root = root.right
        return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not root else self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

class Solution:
    def inorderTraversal(self, r: Optional[TreeNode]) -> List[int]:
        return(f:=lambda r:r and[*f(r.left),r.val,*f(r.right)]or[])(r)

class Solution:
    def inorderTraversal(self, r: Optional[TreeNode]) -> List[int]:
        return(f:=lambda r:r and f(r.left)+[r.val]+f(r.right)or[])(r)

test('''
94. Binary Tree Inorder Traversal
Easy

12680

688

Add to List

Share
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
Accepted
2,256,947
Submissions
3,006,144
''')
