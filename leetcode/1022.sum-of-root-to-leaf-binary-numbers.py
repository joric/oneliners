from lc import *

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/617529173/?envType=daily-question&envId=2026-02-24

class Solution:
    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)

class Solution:
    def sumRootToLeaf(self, t: Optional[TreeNode]) -> int:
        return(f:=lambda t,x:t and((x:=x*2+t.val)and t.left==t.right and x or f(t.left,x)+f(t.right,x))or 0)(t,0)

class Solution:
    def sumRootToLeaf(self, t: Optional[TreeNode]) -> int:
        return(f:=lambda t,x:t and(x:=x*2+t.val)*(t.left==t.right)+f(t.left,x)+f(t.right,x)or 0)(t,0)

class Solution:
    def sumRootToLeaf(self, t: Optional[TreeNode]) -> int:
        return(f:=lambda t,x:t and(f(t.left,x:=x*2+t.val)+f(t.right,x)or x)or 0)(t,0)

test('''
1022. Sum of Root To Leaf Binary Numbers
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0


Other examples:

Input: root = [1]
Output: 1

Input: root = [1,1]
Output: 3

Input: root = [0,1,0,0,null,0,0,null,null,null,1,null,null,null,1]
Output: 5

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
247,844/336.4K
Acceptance Rate
73.7%
Topics
Staff
Tree
Depth-First Search
Binary Tree
Weekly Contest 131
icon
Companies
Hint 1
Find each path, then transform that path to an integer in base 10.
''')
