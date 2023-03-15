from lc import *

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def f(t):
            if not t:
                return 0
            l,r = f(t.left), f(t.right)
            if l & (l+1)==0 and l/2<=r<=l:
                return l+r+1
            if r & (r+1)==0 and r<=l<=r*2+1:
                return l+r+1
            return -1
        return f(root) > 0

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        i = 0
        while q[i]:
            q += (q[i].left,q[i].right)
            i += 1
        return not any(q[i:])

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return next((not any(q[i:]) for i in count() if not(q[i] and (q:=q+[q[i].left,q[i].right]))),q:=[root])

test('''

958. Check Completeness of a Binary Tree
Medium

2433

33

Add to List

Share
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000

Accepted
133,798
Submissions
248,141

''')

