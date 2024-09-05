from lc import *

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        r = []
        def f(x,h):
            if not x:
                return
            if h==len(r):
                r.append([])
            r[h] = [x.val]+r[h] if h%2 else r[h]+[x.val]
            f(x.left,h+1)
            f(x.right,h+1)
        f(root,0)
        return r

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return (r:=[],(f:=lambda x,h:x and (h==len(r) and r.append([]),setitem(r,h,[x.val]+r[h] if h%2 else r[h]+[x.val]),f(x.left,h+1),f(x.right,h+1)))(root,0),r)[-1]

test('''

103. Binary Tree Zigzag Level Order Traversal
Medium

8307

220

Add to List

Share
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Example 4:
Input: root = [0,2,4,1,null,3,-1,5,1,null,6,null,8]
Output: [[0],[4,2],[1,3,-1],[8,6,1,5]]

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
''')

