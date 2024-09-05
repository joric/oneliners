from lc import *

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh = lambda root: 1 + lh(root.left) if root else 0
        rh = lambda root: 1 + rh(root.right) if root else 0
        l,r = lh(root), rh(root)
        return 2**l-1 if l==r else 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        lh = lambda root: 1+lh(root.left) if root else -1
        n,h = 0, lh(root)
        while root:
            if lh(root.right)==h-1:
                n += 1<<h
                root = root.right
            else:
                n += 1<<h-1
                root = root.left
            h -=1
        return n

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 0 if (h:=(lh:=lambda root: 1+lh(root.left) if root else -1)(root))<0 else \
            (1<<h)+self.countNodes(root.right) if lh(root.right)==h-1 else (1<<h-1)+self.countNodes(root.left)


test('''

222. Count Complete Tree Nodes
Medium

6131

348

Add to List

Share
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.

''')
