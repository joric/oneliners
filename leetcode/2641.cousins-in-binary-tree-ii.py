from lc import *

# https://leetcode.com/problems/cousins-in-binary-tree-ii/discuss/5955544/10-lines-clean-and-easy-Python-solution-or-BFS-or-Level-order-traversal-or-O(n)-or-Beats-96

class Solution:
    def replaceValueInTree(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque([(r,r.val)])
        while q:
            s = sum([i[0].val for i in q])
            for _ in range(len(q)):
                t,m = q.popleft()
                t.val = s-m
                a,b = t.left,t.right
                m = (a and a.val or 0)+(b and b.val or 0)
                a and q.append((a,m))
                b and q.append((b,m))
        return r

# https://leetcode.com/problems/cousins-in-binary-tree-ii/discuss/5143153/Python-Traverse-Twice-DFS-and-BFS-Solutions

class Solution:
    def replaceValueInTree(self, t: Optional[TreeNode]) -> Optional[TreeNode]:
        s={}
        def f(t,c):
            if t:
                s[c] = s.get(c,0)+t.val
                f(t.left,c+1)
                f(t.right,c+1)
        def g(t,x,c):
            if t:
                t.val = s[c]-t.val-x
                a = t.left and t.left.val or 0
                b = t.right and t.right.val or 0
                g(t.left,b,c+1)
                g(t.right,a,c+1)
        f(t,0)
        g(t,0,0)
        return t

class Solution:
    def replaceValueInTree(self, t: Optional[TreeNode]) -> Optional[TreeNode]:
        s={};(f:=lambda t,c:t and(setitem(s,c,s.get(c,0)+t.val),f(t.left,c+1),f(t.right,c+1)))(t,0);(g:=lambda t,x,c:t and(setattr(t,'val',s[c]-t.val-x),l:=t.left,r:=t.right,a:=l and l.val or 0,g(l,r and r.val or 0,c+1),g(r,a,c+1)))(t,0,0);return t

test('''
2641. Cousins in Binary Tree II
Medium

782

26

Add to List

Share
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104
Accepted
48,124
Submissions
66,214
''')
