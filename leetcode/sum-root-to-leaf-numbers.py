from lc import *

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node: return 0
            val = val*10 + node.val
            if not (node.left or node.right): return val
            return dfs(node.left, val) + dfs(node.right, val)
        return dfs(root, 0)

# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/762324/Python3-One-liner

class Solution:
    def sumNumbers(self, r: TreeNode, v: int = 0) -> int:
        return 0 if r is None else r.val + 10 * v if r.left is None and r.right is None else self.sumNumbers(r.left, r.val + 10 * v) + self.sumNumbers(r.right, r.val + 10 * v)

# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/706583/Ugly-python-one-liner

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def calc(root, val):
            return 0 if not root else 10 * val + root.val if not any((root.left, root.right)) else calc(root.left, 10 * val + root.val) + calc(root.right, 10 * val + root.val)
        return calc(root, 0)

# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1556025/Python-One-liner-Recursion%3A-Easy-to-understand-with-Explanation

class Solution:
    def sumNumbers(self, root: TreeNode, curr: Optional[int] = 0) -> int:
        return ((self.sumNumbers(root.left, curr*10+root.val) if root.left else 0) + (self.sumNumbers(root.right, curr*10+root.val) if root.right else 0)) if root.left or root.right else (curr*10+root.val)

# mine

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return (f:=lambda t,v:t and (v:=t.val+10*v,f(t.left,v)+f(t.right,v) if (t.left or t.right) else v)[1] or 0)(root,0)

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return (f:=lambda t,v:t and (lambda l,r,v:(l or r) and f(l,v)+f(r,v) or v)(t.left,t.right,t.val+10*v) or 0)(root,0)

# updated 2024-04-15

class Solution:
    def sumNumbers(self, r: TreeNode) -> int:
        return(f:=lambda t,v:t and(lambda l,r,v:(l or r)and f(l,v)+f(r,v)or v)(t.left,t.right,t.val+10*v)or 0)(r,0)

class Solution:
    def sumNumbers(self, r: TreeNode) -> int:
        return(f:=lambda t,v:t and(f(l:=t.left,v:=t.val+10*v)+f(r:=t.right,v)or v)or 0)(r,0)

test('''

129. Sum Root to Leaf Numbers
Medium

5452

96

Add to List

Share
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [1,2,3]
Output: 25

Explanation:

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026

Example 3:
Input: root = [0,1]
Output: 1

Explanation:

The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.

Accepted
535,554
Submissions
903,611


''')
