from lc import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root, 0)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return root and 1 + max(map(self.maxDepth, (root.left, root.right))) or 0

test('''

104. Maximum Depth of Binary Tree
Easy

9884

159

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
''')
