from lc import *

# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/discuss/3773664/Short-simple-and-easy-to-understand-Python-code.

class Solution:
    def averageOfSubtree(self, r: Optional[TreeNode]) -> int:
        def f(x,v):
            if not x:
                return 0,0,0
            l = f(x.left,v)
            r = f(x.right,v)
            s = l[0]+r[0]+x.val
            t = l[1]+r[1]+1
            v = l[2]+r[2]+(s//t==x.val)
            return s,t,v
        return f(r,0)[2]

class Solution:
    def averageOfSubtree(self, r: Optional[TreeNode]) -> int:
        return (g:=lambda x,v:x and(lambda a,b,c,d,e,f:(s:=a+d+x.val,t:=b+e+1,v:=c+f+(s//t==x.val),(s,t,v))[-1])(*g(x.left,v),*g(x.right,v))or(0,0,0))(r,0)[2]

# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/discuss/2020880/Decorated-Python

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def subtree(f):
            @cache
            def g(root):
                return f(root) + g(root.left) + g(root.right) if root else 0
            return g
        @subtree
        def sum(root):
            return root.val
        @subtree
        def number(root):
            return 1
        @subtree
        def equals_average(root):
            return root.val == sum(root) // number(root)
        return equals_average(root)

class Solution:
    def averageOfSubtree(self, r: Optional[TreeNode]) -> int:
        t=lambda f:(g:=lambda r:r and f(r)+g(r.left)+g(r.right)or 0);s,n=t(lambda r:r.val),t(lambda r:1);return(t(lambda r:r.val==s(r)//n(r)))(r)

class Solution:
    def averageOfSubtree(self, r: Optional[TreeNode]) -> int:
        return((t:=lambda f:(g:=lambda r:r and f(r)+g(r.left)+g(r.right)or 0))(lambda r:r.val==(t(lambda r:r.val))(r)//(t(lambda r:1))(r)))(r)

class Solution:
    def averageOfSubtree(self, r: Optional[TreeNode]) -> int:
        t=lambda f:(g:=lambda r:r and f(r)+g(r.left)+g(r.right)or 0);return(t(lambda r:r.val==(t(lambda r:r.val))(r)//(t(lambda r:1))(r)))(r)

test('''
2265. Count Nodes Equal to Average of Subtree
Medium

1275

24

Add to List

Share
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 

Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
''')

