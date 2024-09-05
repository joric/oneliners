from lc import *

# https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/148890/python-3-lines-dfs-solution-w-a-very-simple-approach/2242278

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchBST(root.left,val) if root and val<root.val else self.searchBST(root.right,val) if root and val>root.val else root

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return root if not root or root.val==val else self.searchBST((root.left,root.right)[val>root.val],val)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return root and(self.searchBST((root.left,root.right)[val>root.val],val)if root.val!=val else root)

class Solution:
    def searchBST(self, r: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        return(f:=lambda r,v:r and(f((r.left,r.right)[v>r.val],v)if r.val!=v else r))(r,v)

class Solution:
    def searchBST(self, r: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        return(f:=lambda r:r and(r.val==v and r or f(r.left)or f(r.right)))(r)

test('''
700. Search in a Binary Search Tree
Easy

5769

184

Add to List

Share
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
Accepted
796,627
Submissions
1,005,383
''')