from lc import *

# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/solutions/438239/python-hacks/?envType=daily-question&envId=2025-02-21

class FindElements:
    def __init__(self, root):
        def v(r, x):
            return r and {x} | v(r.left, 2*x+1) | v(r.right, 2*x+2) or set()
        self.find = v(root, 0).__contains__

class FindElements:
    def __init__(self, r):
        self.find = lambda t:reduce(lambda n, b: n and (n.left, n.right)[int(b)], bin(t+1)[3:], r)!=None

# tests-suite compatible (needs type annotation for the treenode)

class FindElements:
    def __init__(self, r: Optional[TreeNode]):
        self.r = r
    def find(self, t: int) -> bool:
        return t in(f:=lambda r,x:r and{x}|f(r.left,2*x+1)|f(r.right,2*x+2)or set())(self.r, 0)

class FindElements:
    def __init__(self, r: Optional[TreeNode]):
        self.r = r
    def find(self, t: int) -> bool:
        return reduce(lambda n, b: n and (n.left, n.right)[int(b)], bin(t+1)[3:],self.r)!=None

# TODO make it work in lc, perhaps "if name not in dir(classname)" is the issue

FindElements=type('',(),{'__init__':lambda s,r:setattr(s,'r',r),'find':lambda s,t:None!=reduce(lambda n,b:n and(n.left,n.right)[int(b)],bin(t+1)[3:],s.r)})

class FindElements:__init__=lambda s,r:setattr(s,'find',lambda t:bool(reduce(lambda n,b:n and(n.left,n.right)[int(b)],bin(t+1)[3:],r)))

test('''
1261. Find Elements in a Contaminated Binary Tree
Medium
Topics
Companies
Hint
Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 

Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:


Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106
''', classname=FindElements, cast=lambda name,v:TreeNode.parse(v) if name=='r' else v)
