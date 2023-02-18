from lc import *

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return root and TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return (f:=lambda x:x and TreeNode(x.val,f(x.right),f(x.left)))(root)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return (f:=lambda x:x and [*map(setattr,(x,x),('left','right'),(f(x.right),f(x.left)))] and x)(root)

test('''

226. Invert Binary Tree
Easy

10978

156

Add to List

Share
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
''')

