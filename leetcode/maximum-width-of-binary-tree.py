from lc import *

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        r = 0
        q = deque([(root,0)])
        while q:
            j = q[0][1]
            for _ in range(len(q)):
                n,i = q.popleft()
                if n.left:
                    q.append((n.left,2*i))
                if n.right:
                    q.append((n.right,2*i+1))
                r = max(r, i-j+1)
        return r

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
            r,q = 0, [(1,root)]
            while q:
                r = max(r,q[-1][0]-q[0][0]+1)
                q = [v for x,n in q for v in enumerate((n.left,n.right),2*x) if v[1]]
            return r

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return next((r for _ in count() if not(q and (r:=max(r,q[-1][0]-q[0][0]+1),q:=[v for x,n in q for v in enumerate((n.left,n.right),2*x) if v[1]]))),(r:=0,q:=[(1,root)]))

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        d = defaultdict(list)
        def f(l,p,r):
            if r:
                d[l].append(p)
                f(l+1,2*p,r.left)
                f(l+1,2*p+1,r.right)
        f(0,0,root)
        return max(max(v)-min(v)+1 for v in d.values())

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return (d:=defaultdict(list),(f:=lambda l,p,r:r and (d[l].append(p),f(l+1,2*p,r.left),f(l+1,2*p+1,r.right)))(0,0,root)) and max(max(v)-min(v)+1 for v in d.values())

test('''
662. Maximum Width of Binary Tree
Medium

6480

885

Add to List

Share
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Example 4:
Input: root = [1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2]
Output: 8

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
Accepted
246,581
Submissions
605,005
Seen this question in a real interview before?

Yes

No


''')

