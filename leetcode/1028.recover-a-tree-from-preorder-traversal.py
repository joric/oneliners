from lc import *

# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/solutions/2594784/short-8-line-recursive-python-solution/?envType=daily-question&envId=2025-02-22

class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        p = [(len(x),int(y))for x,y in re.findall(r'(-*)(\d+)',s)[::-1]]
        def f(d):
            if p and p[-1][0]>d:
                x,y = p.pop()
                return TreeNode(y,f(x),f(x))
        return f(-1)

class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        p=[(len(x),int(y))for x,y in re.findall(r'(-*)(\d+)',s)[::-1]];return(f:=lambda d:p and d<p[-1][0]and next(TreeNode(y,f(x),f(x))for x,y in[p.pop()])or None)(-1)

class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        p=[(len(x),int(y))for x,y in re.findall('(-*)(\d+)',s)[::-1]];return(f:=lambda d:p and d<p[-1][0]and TreeNode((t:=p.pop())[1],f(t[0]),f(t[0]))or None)(-1)

test('''
1028. Recover a Tree From Preorder Traversal
Solved
Hard
Topics
Companies
Hint
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
57.4K
Submissions
76.1K
Acceptance Rate
75.4%
Topics
String
Tree
Depth-First Search
Binary Tree
Companies
Hint 1
Do an iterative depth first search, parsing dashes from the string to inform you how to link the nodes together.
''')
