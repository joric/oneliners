from lc import *

# TODO: implement tests

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/155806/Python-iterative-and-recursive-solution-with-explanation

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)
        return res[::-1]

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return res
        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)
        recursion(root, res)
        return res

class Solution:
    def postorder(self, t: 'Node') -> List[int]:
        r = []
        def f(t):
            if t:
                for c in t.children:
                    f(c)
                r.append(t.val)
        f(t)
        return r

class Solution:
    def postorder(self, t: 'Node') -> List[int]:
        return(f:=lambda t:t and[*chain(*map(f,t.children))]+[t.val]or[])(t)

class Solution:
    def postorder(self, t: 'Node') -> List[int]:        
        return(f:=lambda t:t and[*chain(*map(f,t.children)),t.val]or[])(t)

test('''
590. N-ary Tree Postorder Traversal
Easy

2343

100

Add to List

Share
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?

Accepted
264,513
Submissions
338,661
''')
