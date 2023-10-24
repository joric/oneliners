from lc import *

# https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/99000/Python-BFS

class Solution:
    def largestValues(self, r: Optional[TreeNode]) -> List[int]:
        m,q=[],[r]
        while any(q):
            m.append(max(x.val for x in q))
            q=[c for x in q for c in (x.left,x.right)if c]
        return m

class Solution:
    def largestValues(self, r: Optional[TreeNode]) -> List[int]:
        m,q=[],[r];return next(m for _ in count()if not(any(q)and(m.append(max(x.val for x in q)),q:=[c for x in q for c in (x.left,x.right)if c])))

test('''
515. Find Largest Value in Each Tree Row
Medium

3088

103

Add to List

Share
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-2^31 <= Node.val <= 2^31 - 1
''')

