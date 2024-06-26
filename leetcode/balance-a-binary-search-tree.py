from lc import *

# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/551956/Python-3-DFS-(in-order)-extraction-and-balanced-tree-building

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ns = dfs(root)
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(l, m-1), build(m + 1, r)
            return root
        return build(0, len(ns) - 1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        a=(f:=lambda x:x and f(x.left)+[x.val]+f(x.right)or[])(t);return(g:=lambda l,r:l<=r and TreeNode(a[m:=(l+r)//2],g(l,m-1),g(m+1,r))or None)(0,len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        a=sorted(filter(None,t._tree_node_to_array()));return(g:=lambda l,r:l<=r and type(t)(a[m:=(l+r)//2],g(l,m-1),g(m+1,r))or None)(0,len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        return(g:=lambda v:v and type(t)(v[m:=(len(v)-1)//2],g(v[:m]),g(v[m+1:]))or None)(sorted(filter(None,t._tree_node_to_array())))

test('''
1382. Balance a Binary Search Tree
Medium

3313

80

Add to List

Share
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
Accepted
188,610
Submissions
226,966
''')
