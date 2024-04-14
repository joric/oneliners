from lc import *

# https://leetcode.com/problems/sum-of-left-leaves

class Solution:
    def sumOfLeftLeaves(self, r: Optional[TreeNode]) -> int:
        return(f:=lambda r,l=0:r and(f(r.left,1)+f(r.right)if r.left or r.right else r.val*l)or 0)(r)

class Solution:
    def sumOfLeftLeaves(self, r: Optional[TreeNode]) -> int:
        return(f:=lambda r,t=0:r and(f(u:=r.left,1)+f(v:=r.right)+(not(u or v))*r.val*t)or 0)(r)

test('''
404. Sum of Left Leaves
Easy

5022

290

Add to List

Share
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

More examples:

Input: root = [1,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
Accepted
508,114
Submissions
876,056
''')
