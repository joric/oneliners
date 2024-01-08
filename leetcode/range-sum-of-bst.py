from lc import *

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + (low <= root.val <= high) * root.val if root else 0

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return root and self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + (low <= root.val <= high) * root.val or 0

class Solution:
    def rangeSumBST(s, r: TreeNode, a: int, b: int) -> int:
        return r and r.val*(a<=r.val<=b)+sum(map(s.rangeSumBST,(r.left,r.right),[a]*2,[b]*2))or 0

class Solution:
    def rangeSumBST(s, r: TreeNode, a: int, b: int) -> int:
        return(f:=lambda r:r and r.val*(a<=r.val<=b)+f(r.left)+f(r.right)or 0)(r)

test('''

938. Range Sum of BST
Easy
4.8K
340
Companies
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.

''')

