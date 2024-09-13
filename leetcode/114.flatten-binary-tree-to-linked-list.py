from lc import *

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1208004/Extremely-Intuitive-O(1)-Space-solution-with-Simple-explanation-Python

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left != None:
                p = curr.left
                while p.right != None:
                    p = p.right
                p.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/274723/5-line-python-recursive

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        right, root.left, root.right = root.right, None, root.left
        end = self.flatten(root.right) if root.right else root
        end.right = right
        return self.flatten(right) if right else end

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1549901/7-lines-python-solution

class Solution:
    def flatten(self, t: Optional[TreeNode]) -> None:
        self.pre = None
        def f(t):
            if t:
                f(t.right)
                f(t.left)
                t.right= self.pre
                t.left = None
                self.pre  = t
        f(t)

class Solution:
    def flatten(s, t: Optional[TreeNode]) -> None:
        a=setattr;s.p=None;(f:=lambda t:t and(f(t.right),f(t.left),a(t,'right',s.p),a(t,'left',None),a(s,'p',t)))(t)

test('''
114. Flatten Binary Tree to Linked List
Medium

12396

566

Add to List

Share
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
Accepted
1,027,560
Submissions
1,550,005
''', inplace=True)
