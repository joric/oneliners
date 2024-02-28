from lc import *

# https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution:
    def findBottomLeftValue(self, r: Optional[TreeNode]) -> int:
        v = []
        def f(r,i):
            len(v)==i and v.append([])
            v[i].append(r.val)
            r.left and f(r.left,i+1)
            r.right and f(r.right,i+1)
        f(r,0)
        return v[-1][0]

# https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-%2B-Java)

class Solution:
    def findBottomLeftValue(self, r: Optional[TreeNode]) -> int:
        q=[r];[q.extend(filter(None,(x.right,x.left)))for x in q];return q[-1].val

class Solution:
    def findBottomLeftValue(self, r: Optional[TreeNode]) -> int:
        q=[r];return[q.extend((x.right,x.left))or x.val for x in q if x][-1]

test('''
513. Find Bottom Left Tree Value
Medium

3354

267

Add to List

Share
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
Accepted
264,111
Submissions
384,188
''')
