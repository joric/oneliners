from lc import *

# https://leetcode.com/problems/recover-binary-search-tree/

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first, self.second, self.prev = None, None, TreeNode(float('-inf')) 
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev.val >= node.val: 
                    self.first = self.first or self.prev
                    self.second = node
                self.prev = node
                inorder(node.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

test('''
99. Recover Binary Search Tree
Medium

7960

260

Add to List

Share
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
Accepted
480,725
Submissions
887,416
''', inplace=True)
