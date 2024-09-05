from lc import *

# https://leetcode.com/problems/middle-of-the-linked-list/discuss/2880828/Python-3-one-line-recursiveiterative

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return next((s for _ in count() if not(f and f.next and (f:=f.next.next,s:=s.next))),(f:=head,s:=head))

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(fast, slow):
            return dfs(fast.next.next, slow.next) if fast and fast.next else (fast, slow)
        return dfs(head, head)[1]

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return (g:=lambda f,s: g(f.next.next, s.next) if f and f.next else (f,s))(head,head)[1]

# updated 2024-03-07

class Solution:
    def middleNode(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return(f:=lambda a,b:a and a.next and f(a.next.next,b.next)or(a,b))(h,h)[1]

class Solution:
    def middleNode(self, h: Optional[ListNode]) -> Optional[ListNode]:
        [h:=h.next for _ in eval(h.serialize(h))[1::2]];return h

test('''

876. Middle of the Linked List
Easy

8012

220

Add to List

Share
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

''')


