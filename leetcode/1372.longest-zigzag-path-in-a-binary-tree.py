from lc import *

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def f(x):
            if not x:
                return 0,0,0
            l = f(x.left)
            r = f(x.right)
            return l[1]+1,r[0]+1,max(max(l),max(r))
        return max(f(root))-1

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        return max((f:=lambda x:x and((l:=f(x.left))[1]+1,(r:=f(x.right))[0]+1,max(max(l),max(r)))or[0]*3)(root))-1

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        return (f:=lambda n,l,r:max(f(n.left,0,l+1),f(n.right,r+1,0)) if n else max(l,r)-1)(root,0,0)

test('''
1372. Longest ZigZag Path in a Binary Tree
Medium

1894

33

Add to List

Share
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
Accepted
61,552
Submissions
97,206
Seen this question in a real interview before?

Yes

No
Create this function maxZigZag(node, direction) maximum zigzag given a node and direction (right or left).
''')

