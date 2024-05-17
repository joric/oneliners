from lc import *

# https://leetcode.com/problems/delete-leaves-with-a-given-value/discuss/484295/Python-simple

class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        if r:
            r.left = self.removeLeafNodes(r.left, t)
            r.right = self.removeLeafNodes(r.right, t)
            if r.val!=t or r.left or r.right:
                return r

class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        return r and(setattr(r,'left',self.removeLeafNodes(r.left,t)),setattr(r,'right',self.removeLeafNodes(r.right,t)))and(r.val!=t or r.left or r.right)and r

# https://leetcode.com/problems/delete-leaves-with-a-given-value/discuss/484312/Python-5-lines-dfs-solution

class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        def f(x):
            if x:
                x.left = f(x.left)
                x.right = f(x.right)
                if x.val!=t or x.left or x.right:
                    return x
        return f(r)

class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        s=setattr;return(f:=lambda x:x and(s(x,'left',f(x.left)),s(x,'right',f(x.right)))and(x.val!=t or x.left or x.right)and x or None)(r)

test('''
1325. Delete Leaves With a Given Value
Medium

2137

37

Add to List

Share
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:



Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
Accepted
95,811
Submissions
128,882
''')

