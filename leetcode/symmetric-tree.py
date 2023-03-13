from lc import *

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        s = [(root.left, root.right)]
        while s:
            a,b = s.pop()
            if a and b and a.val==b.val:
                s += [(a.left,b.right),(a.right,b.left)]
            else:
                return not (a or b)
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(a,b):
            if a and b:
                return a.val==b.val and mirror(a.left,b.right) and mirror(a.right,b.left)
            return not a and not b
        return mirror(root.left,root.right) if root else True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root and (f:=lambda a,b:a.val==b.val and f(a.left,b.right) and f(a.right,b.left) if a and b else not(a or b))(root.left,root.right)

test('''

101. Symmetric Tree
Easy

12396

280

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Example 2:
Input: root = [1,2,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
Accepted
1,532,743
Submissions
2,862,296

''')

