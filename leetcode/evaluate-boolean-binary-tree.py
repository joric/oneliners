from lc import *

# https://leetcode.com/problems/evaluate-boolean-binary-tree/discuss/4387520/Java-one-line-solution

class Solution:
    def evaluateTree(self, r: Optional[TreeNode]) -> bool:
        return self.evaluateTree(r.left) or self.evaluateTree(r.right) if r.val==2 else self.evaluateTree(r.left) and self.evaluateTree(r.right) if r.val==3 else r.val==1

class Solution:
    def evaluateTree(self, r: Optional[TreeNode]) -> bool:
        f=self.evaluateTree;return f(r.left) or f(r.right)if r.val==2 else f(r.left) and f(r.right)if r.val==3 else r.val==1

# https://leetcode.com/problems/evaluate-boolean-binary-tree/discuss/2259612/Python3-Solution-or-Recursion-or-3-line

class Solution:
    def evaluateTree(self, root):
        if root.val <= 1: return root.val
        left, right = self.evaluateTree(root.left), self.evaluateTree(root.right)
        return (left or right) if root.val == 2 else (left and right)

class Solution:
    def evaluateTree(self, t: Optional[TreeNode]) -> bool:
        if t.val<2:
            return t.val
        p = map(self.evaluateTree,(t.left,t.right))
        f = (or_,and_)[t.val-2]
        return f(*p)

class Solution:
    def evaluateTree(self, r: Optional[TreeNode]) -> bool:
        return x if(x:=r.val)<2else(or_,and_)[x-2](*map(self.evaluateTree,(r.left,r.right)))

class Solution:
    def evaluateTree(self, r: Optional[TreeNode]) -> bool:
        return(f:=lambda r:x if(x:=r.val)<2else(or_,and_)[x-2](f(r.left),f(r.right)))(r)

class Solution:
    def evaluateTree(self, r: Optional[TreeNode]) -> bool:
        return(f:=lambda r:x if(x:=r.val)<2else(or_,mul)[x-2](f(r.left),f(r.right)))(r)

test('''
2331. Evaluate Boolean Binary Tree
Easy

979

26

Add to List

Share
You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:


Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
Example 2:

Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.
 

More examples:

Input: root = [3,3,2,0,0,3,2,null,null,null,null,1,3,1,1,null,null,2,1,null,null,null,null,1,1,null,null,null,null,null,null]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 3
Every node has either 0 or 2 children.
Leaf nodes have a value of 0 or 1.
Non-leaf nodes have a value of 2 or 3.
Accepted
77,620
Submissions
98,779
''')
