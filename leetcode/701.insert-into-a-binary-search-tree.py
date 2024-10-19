from lc import *

# https://leetcode.com/problems/insert-into-a-binary-search-tree/

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

# https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/2684040/Python-One-Liner-93.39-Time-and-99.50-Space

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return TreeNode(val) if not root else TreeNode(root.val, root.left, self.insertIntoBST(root.right,val)) if root.val < val else TreeNode(root.val, self.insertIntoBST(root.left,val), root.right)

class Solution:
    def insertIntoBST(self, r: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        return(f:=lambda r,x:TreeNode(x)if not r else TreeNode(r.val,r.left,f(r.right,x))if r.val<x else TreeNode(r.val,f(r.left,x),r.right))(r,v)

test('''
701. Insert into a Binary Search Tree
Medium

5926

179

Add to List

Share
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
Accepted
596,898
Submissions
810,325
''')
