from lc import *

def check(res,exp,head: ListNode):
    def isBalanced(root: TreeNode) -> bool:
        return (f:=lambda x:(((l:=f(x.left))<0 or (r:=f(x.right))<0 or abs(l-r)>1) and -1) or 1+max(l,r) if x else 0)(root)>=0
    return (f:=lambda v:sorted([x for x in v if x is not None]))(res and res.dump() or [])==f(exp) and isBalanced(res)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head or not head.next:
            return TreeNode(head.val) if head else None
        s = f = head
        while f and f.next:
            f = f.next.next
            s.next, s = s.next if f and f.next else None, s.next
        return TreeNode(s.val, self.sortedListToBST(head), self.sortedListToBST(s.next))

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        v = []
        while head:
            v.append(head.val)
            head = head.next
        def f(i,j):
            if i>j:
                return None
            m = (i+j)//2
            return TreeNode(v[m],f(i,m-1),f(m+1,j))
        return f(0,len(v)-1)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return (f:=lambda i,j:None if i>j else TreeNode(v[(m:=(i+j)//2)],f(i,m-1),f(m+1,j)))(0,len(v:=(g:=lambda x:x and [x.val]+g(x.next) or [])(head))-1)

test('''

109. Convert Sorted List to Binary Search Tree
Medium

5629

128

Add to List

Share
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 10^4].
-10^5 <= Node.val <= 10^5

Accepted
419,075
Submissions
724,040

''', check=check

)
