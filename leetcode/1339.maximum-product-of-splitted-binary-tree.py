from lc import *

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/solutions/496817/python-8-lines/

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        r = []
        def f(x):
            if not x:
                return 0
            r.append(x.val + f(x.left) + f(x.right))
            return r[-1]
        s = f(root)
        return max(x * (s - x) for x in r) % (10**9+7)

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        r = []
        f = lambda x:r.append(a:=x.val+f(x.left)+f(x.right)) or a if x else 0
        s = f(root)
        return max((s-x)*x for x in r) % (10**9+7)

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        return (r:=[],s:=(f:=lambda x:r.append(a:=x.val+f(x.left)+f(x.right)) or a if x else 0)(root)) and max((s-x)*x for x in r) % (10**9+7)

# 2026-01-07 POTD

class Solution:
    def maxProduct(self, t: Optional[TreeNode]) -> int:
        r=[];f=lambda x:x and(r.append(a:=x.val+f(x.left)+f(x.right))or a)or 0;s=f(t);return max(x*(s-x)for x in r)%(10**9+7)

test('''
1339. Maximum Product of Splitted Binary Tree
Medium
1.6K
72
Companies
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104

''')
