from lc import *

# https://leetcode.com/problems/path-sum/discuss/36588/Shortest-possible%3A-one-liner
# Pochmann

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:
        return bool(root and (root.left==root.right and root.val==sum
            or self.hasPathSum(root.left, sum-root.val)
            or self.hasPathSum(root.right, sum-root.val)))

class Solution:
    def hasPathSum(self, t: Optional[TreeNode], s: int) -> bool:
        return (f:=lambda t,s:t and ((t.left==t.right and s==t.val) or f(t.left,s-t.val) or f(t.right,s-t.val)))(t,s)

class Solution:
    def hasPathSum(self, t: Optional[TreeNode], s: int) -> bool:
        if not t: return False
        if not t.left and not t.right and t.val==s: return True
        return self.hasPathSum(t.right,s-t.val) or self.hasPathSum(t.left,s-t.val)

class Solution:
    def hasPathSum(self, t: Optional[TreeNode], s: int) -> bool:
        return t and (((r:=s-t.val)==0 and not(t.left or t.right)) or self.hasPathSum(t.left,r) or self.hasPathSum(t.right,r))

class Solution:
    def hasPathSum(self, t: Optional[TreeNode], s: int) -> bool:
        return(f:=lambda t,s:t and(not((r:=s-t.val)or t.left or t.right)or f(t.left,r)or f(t.right,r)))(t,s)

class Solution:
    def hasPathSum(self, t: Optional[TreeNode], s: int) -> bool:
        return(f:=lambda t,s:t and((not(r:=s-t.val)and t.left==t.right)or f(t.left,r)or f(t.right,r)))(t,s)

test('''
112. Path Sum
Easy

9782

1123

Add to List

Share
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
Accepted
1,567,234
Submissions
3,054,226
''')
