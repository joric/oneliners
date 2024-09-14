from lc import *

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def deserialize(str):
        return Node.parse(json.loads(str))

    def parse(arr):
        if not arr:
            return None
        if type(arr) is int:
            return Node(arr)
        nodes = [None if x is None else Node(x) for x in arr]
        kids = nodes[::-1]
        root = kids and kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    # The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

    @staticmethod
    def dump(root):
        q = []
        res = []
        q.append(root)
        while len(q):
            nodes = len(q)
            for _ in range(nodes):
                root = q.pop(0)
                res.append(root and root.val)
                if root:
                    q.append(root.left)
                    q.append(root.right)
            res.append('#')
        res.pop()
        while res and res[-1] is None:
            res.pop()
        return res

    @staticmethod
    def serialize(root):
        return str(Node.dump(root)).replace('None','null') if root else'[]'

    def __repr__(self):
        d = Node.dump(self)
        return f'[{','.join(map(str,d))}]'

class Solution:
    def connect(self, root: 'Optional[Node]', next: 'Node' = None) -> 'Optional[Node]':
        if not root: return None
        root.next = next
        self.connect(root.right, next.left if next else None)
        self.connect(root.left, root.right)
        return root

class Solution:
    def connect(self, t: 'Optional[Node]') -> 'Optional[Node]':
        return(f:=lambda t,n,a=setattr:t and(a(t,'next',n),f(t.right,n and n.left),f(t.left,t.right))and t)(t,None)

test('''
116. Populating Next Right Pointers in Each Node
Medium

9793

308

Add to List

Share
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
Accepted
1,090,752
Submissions
1,715,036
''')
