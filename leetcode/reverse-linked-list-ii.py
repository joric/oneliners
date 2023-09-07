from lc import *

class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        curr = pre.next
        nxt = curr.next
        for i in range(n-m):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
        pre.next.next = nxt
        pre.next = curr
        return dummy.next

class Solution:
    def reverseBetween(self, r: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        c=[(r.val,r:=r.next)[0]for _ in[0]*500if r];return ListNode(','.join(map(str,c[:m-1]+c[m-1:n][::-1]+c[n:])))

class Solution:
    def reverseBetween(self, r: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        c=[(str(r.val),r:=r.next)[0]for _ in[0]*500if r];return ListNode(','.join(c[:m-1]+c[m-1:n][::-1]+c[n:]))

test('''
92. Reverse Linked List II
Medium

9822

446

Add to List

Share
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
''')

