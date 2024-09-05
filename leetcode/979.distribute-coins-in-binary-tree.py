from lc import *

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221930/JavaC%2B%2BPython-Recursive-Solution

class Solution:
    def distributeCoins(self, root: Optional[TreeNode], pre=None) -> int:
        if not root:
            return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre:
            pre.val += root.val - 1
        return res + abs(root.val - 1)

class Solution:
    def distributeCoins(self, r: Optional[TreeNode]) -> int:
        return(f:=lambda r,p=None:r and(x:=f(r.left,r)+f(r.right,r),t:=r.val-1,p and setattr(p,'val',p.val+t),x+abs(t))[3]or 0)(r)

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/222395/Java-Super-Short-Solution-!!!

class Solution:
    def distributeCoins(self, r: Optional[TreeNode]) -> int:
        c=[0];(f:=lambda r:r and(x:=f(r.left)+f(r.right)+r.val-1,setitem(c,0,c[0]+abs(x)))[0]or 0)(r);return c[0]

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/5174311/one-line-solution

class Solution:
    def distributeCoins(self, r: Optional[TreeNode]) -> int:
        def f(n):
            if n:
                l, r = f(n.left), f(n.right)
                c = n.val + l[0] + r[0] - 1
                return (c, l[1] + r[1] + abs(c))
            return (0, 0)
        return f(r)[1]

class Solution:
    def distributeCoins(self, r: Optional[TreeNode]) -> int:
        return(f:=lambda n:n and(c:=n.val+(l:=f(n.left))[0]+(r:=f(n.right))[0]-1,l[1]+r[1]+abs(c))or(0,0))(r)[1]

test('''
979. Distribute Coins in Binary Tree
Medium

5007

182

Add to List

Share
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
 

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
Accepted
119,455
Submissions
163,671
''')