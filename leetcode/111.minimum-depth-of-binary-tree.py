from lc import *

# https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36060/3-lines-in-Every-Language

class Solution:
    def minDepth(s, r: Optional[TreeNode]) -> int:
        return r and 1+(min(d:=[*map(s.minDepth,(r.left,r.right))])or max(d))or 0

test('''
111. Minimum Depth of Binary Tree
Easy

5928

1152

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
''')
