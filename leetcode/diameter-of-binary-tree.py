from lc import *

# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if not root: return 0, -1
            pl, hl = helper(root.left)
            pr, hr = helper(root.right)
            return max(pl, pr, hl + hr + 2), max(hl, hr) + 1
        return helper(root)[0]

# https://leetcode.com/problems/diameter-of-binary-tree/discuss/160845/Python-2-lines

class Solution:
    def diameterOfBinaryTree(self, r: TreeNode) -> int:
        return(f:=lambda r:r and max((h:=lambda r:r and 1+max(h(r.left),h(r.right))or 0)(r.left)+h(r.right),f(r.left),f(r.right))or 0)(r)

# https://leetcode.com/problems/diameter-of-binary-tree/discuss/1127495/8-lines-Python-solution-with-explanation

class Solution:
    def diameterOfBinaryTree(self, r: TreeNode) -> int:
        def f(r):
            if not r:
                return 0,0
            l,p = f(r.left)
            r,q = f(r.right)
            return max(p+q,l,r),max(p,q)+1
        return f(r)[0]

class Solution:
    def diameterOfBinaryTree(self, r: TreeNode) -> int:
        return(f:=lambda r:r and(lambda l,p,r,q:(max(p+q,l,r),max(p,q)+1))(*f(r.left),*f(r.right))or(0,0))(r)[0]

test('''
543. Diameter of Binary Tree
Easy

13144

890

Add to List

Share
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

More examples:

Input: root = [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
Output: 8

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
Accepted
1,325,697
Submissions
2,246,950
''')
