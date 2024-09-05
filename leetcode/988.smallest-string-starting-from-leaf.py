from lc import *

# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/231231/C%2B%2B-1-line-0ms
# does not work
class Solution:
    def smallestFromLeaf(self, r: Optional[TreeNode]) -> str:
        return r and min(self.smallestFromLeaf(r.left), self.smallestFromLeaf(r.right),key=cmp_to_key(lambda a,b:False if a=='' else True if b=='' else a<b))+chr(97+r.val) or ''

# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/328119/Simple-Python-Solution:-top-down-DFS/1199036

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        f = lambda c:chr(97+c)
        def fn(node):
            if not node:
                return [""]
            return [f(node.val) + arr for kid in (node.left, node.right) if kid for arr in fn(kid)] or [f(node.val)]
        return min([s[::-1] for s in fn(root)])

class Solution:
    def smallestFromLeaf(self, r: Optional[TreeNode]) -> str:
        f=lambda r:[chr(97+r.val)+v for x in(r.left,r.right)if x for v in f(x)]or[chr(97+r.val)]if r else'';return min([s[::-1]for s in f(r)])

# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/231102/Bottom-up-vs.-Top-down

class Solution:
    def smallestFromLeaf(self, r: Optional[TreeNode]) -> str:
        return(f:=lambda r,s='':s if(s:=chr(97+r.val)+s)and r.left==r.right else min(x and f(x,s)or'|'for x in(r.left,r.right)))(r)

# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/5036440/one-line-solution

class Solution:
    def smallestFromLeaf(self, n: Optional[TreeNode]) -> str:
        return(f:=lambda n,q:n and (min(f(l:=n.left,q:=chr(97+n.val)+q),f(r:=n.right,q)),q)[l==r==None] or '~')(n,'')

# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/231102/Bottom-up-vs.-Top-down/488319

class Solution:
    def smallestFromLeaf(self, r: TreeNode) -> str:
        def f(r,s):
            if not r:
                return '|'
            s = chr(r.val+97) + s
            if not r.left and not r.right:
                return s
            return min(f(r.left,s),f(r.right,s))
        return f(r,'')

class Solution:
    def smallestFromLeaf(self, r: TreeNode) -> str:
        return(f:=lambda r,s:r and(s:=chr(r.val+97)+s)and(min(f(r.left,s),f(r.right,s))if r.left or r.right else s)or'|')(r,'')

class Solution:
    def smallestFromLeaf(self, r: TreeNode) -> str:
        t=[];(f:=lambda r,s:r and((f(r.left,s:=chr(r.val+97)+s)+f(r.right,s))or t.append(s)or 1)or 0)(r,'');return min(t)

class Solution:
    def smallestFromLeaf(self, r: TreeNode) -> str:
        return min((f:=lambda r,s:r and(f(r.left,s:=chr(r.val+97)+s)+f(r.right,s)or[s])or[])(r,''))

class Solution:
    def smallestFromLeaf(self, r: TreeNode) -> str:
        f=lambda r,s:r and(f(r.left,s:=chr(r.val+97)+s)+f(r.right,s)or[s])or[];return min(f(r,''))

test('''
988. Smallest String Starting From Leaf
Medium

1712

242

Add to List

Share
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
 

Other solutions:

Input: root = [4,0,1,1]
Output: "bae"

Input: root = [0,null,1]
Output: "ba"

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
Accepted
80,321
Submissions
155,039
''')