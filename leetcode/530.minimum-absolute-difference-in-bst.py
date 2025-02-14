from lc import *

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/solutions/338515/python-recursive/

class Solution:
    def getMinimumDifference(self, r: Optional[TreeNode]) -> int:
        return(f:=lambda t,a,b:t and min(f(t.left,a,t.val),f(t.right,t.val,b))or b-a)(r,-inf,inf)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        f=lambda n:n and f(n.left)+[n.val]+f(n.right)or[];return min(b-a for a,b in pairwise(f(root)))

class Solution:
    def getMinimumDifference(self, r: Optional[TreeNode]) -> int:
        f=lambda n:n and f(n.left)+[n.val]+f(n.right)or[];return min(map(sub,f(r)[1:],f(r)))

test('''
530. Minimum Absolute Difference in BST
Easy

3246

162

Add to List

Share
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 10^5
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
''')
