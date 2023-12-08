from lc import *

class Solution:
    def tree2str(self, r: Optional[TreeNode]) -> str:
        return(str(r.val)if r else'')+(''if not r or not r.left and not r.right else'('+self.tree2str(r.left)+')')+('('+self.tree2str(r.right)+')'if r and r.right else '')

# https://leetcode.com/problems/construct-string-from-binary-tree/discuss/2543705/Python-Elegant-and-Short-or-DFS

class Solution:
    def tree2str(self, r: TreeNode) -> str:
        return(f:=lambda r:r and'{}{}{}'.format(r.val,f'({f(r.left)})'*(r.left is not None or r.right is not None),f'({f(r.right)})' * (r.right is not None),)or'')(r)

# https://leetcode.com/problems/construct-string-from-binary-tree/discuss/104056/Short-PythonJava-with-post-processing

class Solution:
    def tree2str(self, r: Optional[TreeNode]) -> str:
        return re.sub('(\(\))+$','',('%d(%s)(%s)'%(r.val,self.tree2str(r.left),self.tree2str(r.right))))if r else''

class Solution:
    def tree2str(self, r: Optional[TreeNode]) -> str:
        return(f:=lambda r:re.sub('(\(\))+$','',('%d(%s)(%s)'%(r.val,f(r.left),f(r.right))))if r else'')(r)

class Solution:
    def tree2str(self, r: Optional[TreeNode]) -> str:
        return(f:=lambda r:re.sub('(\(\))+$','',   '%d(%s)(%s)' % (r.val,f(r.left),f(r.right))     )if r else'')(r)

class Solution:
    def tree2str(self, r: Optional[TreeNode]) -> str:
        return(f:=lambda r:r and re.sub('(\(\))+$','',f'{r.val}({f(r.left)})({f(r.right)})')or'')(r)

test('''
606. Construct String from Binary Tree
Easy

2744

3265

Add to List

Share
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:


Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
Accepted
235,300
Submissions
361,609
''')

