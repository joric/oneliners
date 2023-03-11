from lc import *


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
        return (f:=lambda i,j:i<=j and TreeNode(v[(m:=(i+j)//2)],f(i,m-1),f(m+1,j)) or None)(0,len(v:=(g:=lambda x:x and [x.val]+g(x.next) or [])(head))-1)

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

''')
