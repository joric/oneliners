from lc import *

# https://leetcode.com/problems/flip-equivalent-binary-trees/discuss/253619/Python-One-Line-Recursion

class Solution:
    def flipEquiv(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        return(f:=lambda a,b:bool(not(a or b)or a and b and a.val==b.val and(f(a.left,b.left)and f(a.right,b.right)or f(a.left,b.right)and f(a.right,b.left))))(a,b)

test('''
951. Flip Equivalent Binary Trees
Medium

2318

96

Add to List

Share
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false
 

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
Accepted
154,739
Submissions
230,363
''')
