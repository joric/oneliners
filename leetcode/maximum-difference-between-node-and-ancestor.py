from lc import *

# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

class Solution:
    def maxAncestorDiff(s, r,a=inf,b=-1):
        return r and max(s.maxAncestorDiff(r.left,min(a,r.val),max(b,r.val)),s.maxAncestorDiff(r.right,min(a,r.val),max(b,r.val)))or b-a

class Solution:
    def maxAncestorDiff(self, r: TreeNode) -> int:
        return(f:=lambda r,a,b:r and max(f(r.left,min(a,r.val),max(b,r.val)),f(r.right,min(a,r.val),max(b,r.val)))or b-a)(r,inf,0)

class Solution:
    def maxAncestorDiff(self, r: TreeNode) -> int:
        return(f:=lambda r,a,b:r and max(starmap(f,[(p,min(a,r.val),max(b,r.val))for p in(r.left,r.right)]))or b-a)(r,inf,0)

class Solution:
    def maxAncestorDiff(self, r: TreeNode) -> int:
        return(f:=lambda r,a,b:r and max(map(f,[r.left,r.right],[min(a,r.val)]*2,[max(b,r.val)]*2))or b-a)(r,inf,0)

class Solution:
    def maxAncestorDiff(self, r: TreeNode) -> int:
        return(f:=lambda r,a,b:r and max(f(r.left,x:=min(a,r.val),y:=max(b,r.val)),f(r.right,x,y))or b-a)(r,inf,0)

class Solution:
    def maxAncestorDiff(self, r: Optional[TreeNode]) -> int:
        return(f:=lambda r,a,b:r and max(f(n,min(a,v:=r.val),max(b,v))for n in[r.left,r.right])or b-a)(r,inf,0)

test('''

1026. Maximum Difference Between Node and Ancestor
Medium
2.7K
71
Companies
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7

Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5

''')
