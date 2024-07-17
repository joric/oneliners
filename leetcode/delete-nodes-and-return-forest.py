from lc import *

# https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/656106/python-recursive-clean-explained-in-details-with-tips-10-lines-fast

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d = [],{*d}
        def f(t):
            if t:
                t.left = f(t.left)
                t.right = f(t.right)
                if t.val not in d:
                    return t
                a.append(t.left)
                a.append(t.right)
        a.append(f(r))
        return filter(None,a)

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d,v = [],{*d},('left','right')
        def f(t):
            if t:
                [setattr(t,k,f(getattr(t,k)))for k in v]
                if t.val not in d:
                    return t
                [a.append(getattr(t,k))for k in v]
        a.append(f(r))
        return filter(None,a)

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d,v,g=[],{*d},('left','right'),getattr;f=lambda t:t and([setattr(t,k,f(g(t,k)))for k in v],[[a.append(g(t,k))for k in v]]and None if t.val in d else t)[1];a.append(f(r));return filter(None,a)

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d,v,g=[],{*d},('left','right'),getattr;f=lambda t:t and([setattr(t,k,f(g(t,k)))for k in v],[a.extend([g(t,k)for k in v])]and None if t.val in d else t)[1];a.append(f(r));return filter(None,a)

# https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d = [],{*d}
        def f(t,i):
            if t:
                e = t.val in d
                not e and i and a.append(t)
                t.left, t.right = f(t.left,e), f(t.right,e)
                if not e:
                    return t
        f(r,1)
        return a

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d=[],{*d};(f:=lambda t,i:t and(not(e:=t.val in d)and i and a.append(t)or[setattr(t,k,f(getattr(t,k),e))for k in('left','right')]and(t,None)[e]))(r,1);return a

class Solution:
    def delNodes(self, r: Optional[TreeNode], d: List[int]) -> List[TreeNode]:
        a,d=[],{*d};(f:=lambda t,i=1:t and(not(e:=t.val in d)and i and a.append(t)or f==exec('t.left,t.right=f(t.left,e),f(t.right,e)')or(t,None)[e]))(r);return a

test('''
1110. Delete Nodes And Return Forest
Medium

4101

117

Add to List

Share
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Other examples:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
Accepted
253,124
Submissions
361,244
''',
check=lambda res,exp,*args: len(res)==len(exp)and all(a==b for a,b in zip(*map(sorted,map(str,(res,exp)))))
)
