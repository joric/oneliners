from lc import *

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return (f:=lambda r:[[r.val]] + [a+b for a,b in zip_longest(f(r.left), f(r.right), fillvalue=[])] if r else [])(root)[::-1]

test('''

107. Binary Tree Level Order Traversal II
Medium

3897

304

Add to List

Share
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

''')
