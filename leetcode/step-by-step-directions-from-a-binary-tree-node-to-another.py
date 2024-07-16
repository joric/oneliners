from lc import *

# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612105/3-Steps

class Solution:
    def getDirections(self, r: Optional[TreeNode], s: int, d: int) -> str:
        a,b=[],[]
        def f(t, x, p):
            if t.val == x:
                return True
            if t.left and f(t.left, x, p):
                p += 'L'
            elif t.right and f(t.right, x, p):
                p += 'R'
            return p
        f(r,s,a)
        f(r,d,b)
        while a and b and a[-1] == b[-1]:
            a.pop()
            b.pop()
        return ''.join('U'*len(a))+''.join(b[::-1])

class Solution:
    def getDirections(self, r: Optional[TreeNode], s: int, d: int) -> str:
        a,b=[],[];f=lambda t,x,p:t.val==x or(t.left and(f(t.left,x,p)and[p.append('L')])or t.right and f(t.right,x,p)and p.append('R'))or p;f(r,s,a);f(r,d,b);all(a and b and a[-1]==b[-1]and(a.pop(),b.pop())for _ in count());return''.join('U'*len(a))+''.join(b[::-1])

class Solution:
    def getDirections(self, r: Optional[TreeNode], s: int, d: int) -> str:
        a,b=[],[];f=lambda t,x,p:t.val==x or(t.left and(f(t.left,x,p)and[p.append('L')])or t.right and f(t.right,x,p)and p.append('R'))or p;f(r,s,a);f(r,d,b);[a[-1:]==b[-1:]and(a.pop(),b.pop())for _ in a+b];return''.join('U'*len(a))+''.join(b[::-1])

test('''
2096. Step-By-Step Directions From a Binary Tree Node to Another
Medium

2431

128

Add to List

Share
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.


Other examples:

Input: root = [1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3], startValue = 6, destValue = 15
Output: "UURR"

Input: root = [12,8,2,9,null,4,6,17,15,1,null,7,null,null,null,18,16,null,null,13,5,null,null,null,null,19,14,11,null,null,null,null,10,3], startValue = 13, destValue = 5
Output: "UR"

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
Accepted
109,777
Submissions
219,591
''')
