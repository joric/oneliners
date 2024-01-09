from lc import *

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return(f:=lambda l,r:l if not r else l+[r.val] if not r.left and not r.right else f(f(l,r.left),r.right))([],root1)==f([],root2)

class Solution:
    def leafSimilar(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        return(f:=lambda l,r:l if not r else l+[r.val] if not (r.left or r.right) else f(f(l,r.left),r.right))([],a)==f([],b)


class Solution:
    def leafSimilar(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        return(f:=lambda l,r:l if not r else l+[r.val] if not (r.left or r.right) else f(f(l,r.left),r.right))([],a)==f([],b)

# https://leetcode.com/problems/leaf-similar-trees/discuss/152873/4-line-Python-Solution

class Solution:
    def leafSimilar(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        def f(r):
            if not r:
                return []
            if not (r.left or r.right):
                return [r.val]
            return f(r.left)+f(r.right)
        return f(a)==f(b)

class Solution:
    def leafSimilar(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        def f(r):
            return []if not r else f(r.left)+f(r.right)if(r.left or r.right)else[r.val]
        return f(a)==f(b)

class Solution:
    def leafSimilar(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        return(f:=lambda r:r and(f(r.left)+f(r.right)if(r.left or r.right)else[r.val])or[])(a)==f(b)

class Solution:
    def leafSimilar(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        return(f:=lambda r:r and(f(r.left)+f(r.right)if r.left or r.right else[r.val])or[])(a)==f(b)

test('''

872. Leaf-Similar Trees
Easy
2K
59
Companies
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Example 3:

Input: root1 = [1,2], root2 = [2,2]
Output: true

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

''')
