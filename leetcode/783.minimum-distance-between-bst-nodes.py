from lc import *

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        return (v:=(f:=lambda x:x and f(x.left)+[x.val]+f(x.right) or [])(root)) and min(a-b for a,b in zip(v[1:],v))


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        return (f:=lambda x,a,b:x and min(f(x.left,a,x.val),f(x.right,x.val,b)) or b-a)(root,-inf,inf)

test('''
783. Minimum Distance Between BST Nodes
Easy

2035

341

Add to List

Share
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 10^5
''')