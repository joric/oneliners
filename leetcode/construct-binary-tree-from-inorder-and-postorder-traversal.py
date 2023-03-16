from lc import *

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return (f:=lambda i,p:TreeNode(p[-1],f(i[:k],p[:k]),f(i[k+1:],p[k:-1])) if (k:=i.index(p[-1]) if i else -1)>-1 else None)(inorder,postorder)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return (f:=lambda i,p:None if (k:=i.index(p[-1]) if i else -1)<0 else TreeNode(p[-1],f(i[:k],p[:k]),f(i[k+1:],p[k:-1])))(inorder,postorder)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return (f:=lambda i,p:TreeNode(p[-1],f(i[:(k:=i.index(p[-1]))],p[:k]),f(i[k+1:],p[k:-1])) if i else None)(inorder,postorder)

test('''

106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

6113

88

Add to List

Share
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

Accepted
478,062
Submissions
815,563

''')
