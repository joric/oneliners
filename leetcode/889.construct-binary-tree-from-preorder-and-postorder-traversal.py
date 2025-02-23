from lc import *

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solutions/278586/easy-6-line-python-recursive/?envType=daily-question&envId=2025-02-23

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        if pre and post and pre[0] in post:
            rootval = pre.pop(0)
            root = TreeNode(rootval)
            root.left = self.constructFromPrePost(pre, post[:post.index(rootval)])
            root.right = self.constructFromPrePost(pre, post[:post.index(rootval)])
            return root

class Solution:
    def constructFromPrePost(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        return(f:=lambda a,b:a and a[0]in b and TreeNode(x:=a.pop(0),f(a,b:=b[:b.index(x)]),f(a,b))or None)(a,b)

class Solution:
    def constructFromPrePost(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        return(f:=lambda a,b:{*a}&{*b}and TreeNode(x:=a.pop(0),f(a,b:=b[:b.index(x)]),f(a,b))or None)(a,b)

class Solution:
    def constructFromPrePost(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        return(f:=lambda b:{*a}&{*b}and TreeNode(x:=a.pop(0),f(b:=b[:b.index(x)]),f(b))or None)(b)

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solutions/6457261/4-line-code-simple-recursive-apporch/

class Solution:
    def __init__(self):
        self.i = 0
        self.j = 0
    def constructFromPrePost(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        r = TreeNode(a[self.i])
        self.i += 1
        if r.val != b[self.j]:
            r.left = self.constructFromPrePost(a, b)
        if r.val != b[self.j]:
            r.right = self.constructFromPrePost(a, b)
        self.j += 1
        return r

class Solution:
    def constructFromPrePost(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        def f():
            x = a.pop(0)
            r = TreeNode(x, x!=b[0]and f()or None, x!=b[0]and f()or None)
            b.pop(0)
            return r
        return f()

class Solution:
    def constructFromPrePost(self, a: List[int], b: List[int]) -> Optional[TreeNode]:
        return(f:=lambda x:x!=b[0]and(TreeNode(x:=a.pop(0),f(x),f(x)),b.pop(0))[0]or None)(0)

test('''
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium
Topics
Companies
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
111.4K
Submissions
154.6K
Acceptance Rate
72.1%
Topics
Array
Hash Table
Divide and Conquer
Tree
Binary Tree
''')
