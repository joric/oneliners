from lc import *

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return (f:=lambda r:not r or r.val==root.val and f(r.left) and f(r.right))(root)

test('''

965. Univalued Binary Tree
Easy

1589

60

Add to List

Share
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100

''')

