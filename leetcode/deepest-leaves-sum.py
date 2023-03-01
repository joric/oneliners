from lc import *

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        if root:
            q.append(root)
        while q:
            n = len(q)
            if n:
                res = 0
            for i in range(n):
                root = q.popleft()
                res += root.val
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return res

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def level(node):
            if not node:
                return 0
            return 1 + max(level(node.left), level(node.right))
        def dfs(node, i):
            if not node:
                return 0
            if i==0:
                return node.val
            return dfs(node.left, i-1) + dfs(node.right, i-1)
        return dfs(root, level(root))

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return (dfs:=lambda node,i:0 if not node else dfs(node.left,i-1) +
            dfs(node.right,i-1) if i else node.val)(root,(level:=lambda node:
            max(level(node.left),level(node.right))+1 if node else 0)(root)-1)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return (f:=lambda a: f(b) if (b:=[c for n in a for c in (n.left,n.right) if c]) else sum(n.val for n in a))([root])


test('''
Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

''')
