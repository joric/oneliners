from lc import *

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map

class Solution:
    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> TreeNode:
        def f(i):
            if i:
                j = i.index(p.pop(0))
                t = TreeNode(i[j])
                t.left = f(i[0:j])
                t.right = f(i[j+1:])
                return t
        return f(i)

class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> TreeNode:
        return(f:=lambda i:i and TreeNode(i[j:=i.index(p.pop(0))],f(i[:j]),f(i[j+1:]))or None)(i)

test('''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

15160

519

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
Accepted
1,332,430
Submissions
2,053,257
''')
