from lc import *

# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/5372244/Python-3-one-line-and-DSW

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def vine_to_tree(root, size):
            leaves = size + 1 - int(2**int(log2(size+1)))
            compress(root, leaves)
            size -= leaves
            while size > 1:
                size //= 2
                compress(root, size)

        def compress(root, count):
            scanner = root
            for _ in range(count):
                child = scanner.right
                scanner.right = child.right
                scanner = scanner.right
                child.right = scanner.left
                scanner.left = child

        def tree_to_vine(root):
            tail = root
            rest = tail.right
            size = 0
            while rest:
                if not rest.left:
                    tail = rest
                    rest = rest.right
                    size += 1
                else:
                    temp = rest.left
                    rest.left = temp.right
                    temp.right = rest
                    rest = temp
                    tail.right = temp
            return size

        dummy = TreeNode(0, None, root)
        size = tree_to_vine(dummy)
        vine_to_tree(dummy, size)
        return dummy.right

# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/551956/Python-3-DFS-(in-order)-extraction-and-balanced-tree-building

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        a = dfs(root)
        def build(l,r):
            if l>r:
                return None
            m = (l+r) // 2
            return TreeNode(a[m], build(l,m-1), build(m+1,r))
        return build(0, len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        a=(g:=lambda x:x and g(x.left)+[x.val]+g(x.right)or[])(t);return(f:=lambda l,r:l<=r and TreeNode(a[m:=(l+r)//2],f(l,m-1),f(m+1,r))or None)(0,len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        a=sorted(filter(None,t._tree_node_to_array()));return(f:=lambda l,r:l<=r and type(t)(a[m:=(l+r)//2],f(l,m-1),f(m+1,r))or None)(0,len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        return(f:=lambda a:a and type(t)(a[m:=~-len(a)//2],f(a[:m]),f(a[m+1:]))or None)(sorted(filter(None,t._tree_node_to_array())))

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
''',
check = lambda res,exp,args: (f:=lambda x:(((l:=f(x.left))<0 or (r:=f(x.right))<0 or abs(l-r)>1) and -1) or 1+max(l,r) if x else 0)(res)>=0
)
