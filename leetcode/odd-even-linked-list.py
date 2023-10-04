from lc import *

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        o = head
        n = head.next
        e = n
        while e and e.next:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next
        o.next = n
        return head

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head and (o:=head,n:=o.next,e:=n) and next(setattr(o,'next',n) for _ in count() if not(e and e.next and (setattr(o,'next', o.next.next),e.__setattr__('next',e.next.next),o:=o.next,e:=e.next))) or head

class Solution:
    def oddEvenList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h and(o:=h,n:=o.next,e:=n)and next(setattr(o,'next',n)for _ in count()if not(e and e.next and(setattr(o,'next',o.next.next),setattr(e,'next',e.next.next),o:=o.next,e:=e.next)))or h



test('''

328. Odd Even Linked List
Medium
6.6K
401
Companies
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-10^6 <= Node.val <= 10^6

''')


