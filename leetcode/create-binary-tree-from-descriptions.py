from lc import *

# https://leetcode.com/problems/create-binary-tree-from-descriptions/discuss/1823804/Python-Solution

class Solution:
    def createBinaryTree(self, d: List[List[int]]) -> Optional[TreeNode]:
        s,m=set(),{}
        for p,c,e in d:
            v = m.setdefault(p,TreeNode(p))
            w = m.setdefault(c,TreeNode(c))
            if e:
                v.left = w
            else:
                v.right = w
            s.add(c)
        return m[({*m}-s).pop()]

class Solution:
    def createBinaryTree(self, d: List[List[int]]) -> Optional[TreeNode]:
        s,m,t=set(),{},TreeNode;f=m.setdefault;[setattr(f(p,t(p)),('right','left')[e],f(c,t(c)))or s.add(c)for p,c,e in d];return m[({*m}-s).pop()]

test('''
2196. Create Binary Tree From Descriptions
Medium

1009

21

Add to List

Share
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 

Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
Accepted
47,207
Submissions
62,197
''')
