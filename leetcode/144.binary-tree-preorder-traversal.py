from lc import *

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (f:=lambda r:r and [r.val]+f(r.left)+f(r.right) or [])(root)

test('''

144. Binary Tree Preorder Traversal
Easy

5579

150

Add to List

Share
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
''')