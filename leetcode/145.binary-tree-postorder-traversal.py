from lc import *

# https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not root else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

class Solution:
    def postorderTraversal(self, r: Optional[TreeNode]) -> List[int]:
        return(f:=lambda t:t and f(t.left)+f(t.right)+[t.val]or[])(r)

test('''
145. Binary Tree Postorder Traversal
Easy

6931

193

Add to List

Share
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
''')