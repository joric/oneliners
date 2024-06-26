from lc import *

# https://leetcode.com/problems/balance-a-binary-search-tree
# dsw from wiki https://en.wikipedia.org/wiki/Day%E2%80%93Stout%E2%80%93Warren_algorithm

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

        root = TreeNode(0, None, root)
        size = tree_to_vine(root)
        vine_to_tree(root, size)
        return root.right

# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/2192894/Python-DSW-solution

class Solution:
    # Apply Day–Stout–Warren algorithm
    # Procedure:
    # 1. Convert the tree into a vine:
        # a. dummy node: dummy.right = root
        # b. if dummy.right.left: rightRotate(dummy.right)
        # c. else: dummy = dummy.right
    # 2. left rotate (number of last row nodes) times
    # 3. for cumulative m = number of nodes in complete rows, go back to dummy and rotate m//2 times. Update m to be m//2
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def leftRotate(z):
            y = z.right
            T2 = y.left
            # Perform rotation
            y.left = z
            z.right = T2
            return y
        def rightRotate(z):
            y = z.left
            T3 = y.right
            # Perform rotation
            y.right = z
            z.left = T3
            # Return the new root
            return y
        # Convert to a vine
        dummy = TreeNode(- float('Inf'), None, root)
        temp = dummy
        count = 0
        while temp.right:
            if temp.right.left:
                temp.right = rightRotate(temp.right)
            else:
                temp = temp.right
                count += 1
        # Decide how many nodes are in the last row
        last_row = count
        m = 0
        row = 0
        while last_row >= pow(2,row):
            last_row -= pow(2,row)
            m += pow(2,row)
            row += 1
        # Take care of the last row nodes
        temp = dummy
        for i in range(last_row):
            if temp.right.right:
                temp.right = leftRotate(temp.right)
            temp = temp.right
        # Final balancing
        j = m // 2
        while j > 0:
            temp = dummy
            for i in range(j):
                if temp.right.right:
                    temp.right = leftRotate(temp.right)
                temp = temp.right
            j = j // 2
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
        a=(f:=lambda x:x and f(x.left)+[x.val]+f(x.right)or[])(t);return(g:=lambda l,r:l<=r and TreeNode(a[m:=(l+r)//2],g(l,m-1),g(m+1,r))or None)(0,len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        a=sorted(filter(None,t._tree_node_to_array()));return(g:=lambda l,r:l<=r and type(t)(a[m:=(l+r)//2],g(l,m-1),g(m+1,r))or None)(0,len(a)-1)

class Solution:
    def balanceBST(self, t: TreeNode) -> TreeNode:
        return(g:=lambda a:a and type(t)(a[m:=~-len(a)//2],g(a[:m]),g(a[m+1:]))or None)(sorted(filter(None,t._tree_node_to_array())))

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
