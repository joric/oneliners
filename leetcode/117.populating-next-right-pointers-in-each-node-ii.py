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
                    root.left and q.append(root.left)
                    root.right and q.append(root.right)
            res.append('#')
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
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if not root:
            return None
        q.append(root)
        while q:
            n = len(q)
            prev = None
            for i in range(n):
                node = q.popleft()
                node.next = None
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                      q.append(node.right)
        return root

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/670989/Python-in-10-lines-recursive

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def f(n,c):
            while n and not (n.left or n.right):
                n = n.next
            if n:
                c.next = n.left or n.right
        if root:
            if root.left and root.right: root.left.next = root.right
            elif root.left and root.next: f(root.next, root.left)
            if root.next and root.right: f(root.next, root.right)
            self.connect(root.right)
            self.connect(root.left)
        return root

# convert bfs to recursive

class Solution:
    def connect(self, r: 'Node') -> 'Node':
        a,q=setattr,deque();r and q.append(r);(f:=lambda:(n:=len(q),p:=None,[(t:=q.popleft(),a(t,'next',None),p and a(p,'next',t),p:=t,t.left and q.append(t.left),t.right and q.append(t.right))for i in range(n)],q and f()))();return r

test('''
117. Populating Next Right Pointers in Each Node II
Medium

5878

323

Add to List

Share
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
Accepted
666,718
Submissions
1,245,898
''')
