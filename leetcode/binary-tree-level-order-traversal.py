from lc import *

class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            n = len(q)
            level = []
            for i in range(n):
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(level)
        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return [[root.val]] + [a+b for a,b in zip_longest(self.levelOrder(root.left), self.levelOrder(root.right), fillvalue=[])] if root else []

test('''
102. Binary Tree Level Order Traversal
Medium

11296

214

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
''')
