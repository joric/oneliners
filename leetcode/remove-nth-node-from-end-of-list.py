from lc import *

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

class Solution:
    def removeNthFromEnd(self, h: ListNode, n: int) -> ListNode:
        r=[(h.val,h:=h.next)[0]for _ in[1]*30 if h];p=r[:len(r)-n]+r[len(r)-n+1:];return p and ListNode(','.join(map(str,p)))

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/2989192/3-Line-solution-based-on-one-of-VenomIL's-solutions

class Solution:
    def removeNthFromEnd(self, h: ListNode, n: int) -> ListNode:
        k=[n]
        def f(h):
            if not h:
                return None
            setattr(h,'next',f(h.next))
            setitem(k,0,k[0]-1)
            return h if k[0] else h.next
        return f(h)

class Solution:
    def removeNthFromEnd(self, h: ListNode, n: int) -> ListNode:
        k=[n];return(f:=lambda h:h and(setattr(h,'next',f(h.next)),setitem(k,0,k[0]-1))and(k[0]and h or h.next))(h)

class Solution:
    def removeNthFromEnd(self, h: ListNode, n: int) -> ListNode:
        k=[n];return(f:=lambda h:h and(setattr(h,'next',f(h.next)),setitem(k,0,k[0]-1),k[0]and h or h.next)[2])(h)

test('''
19. Remove Nth Node From End of List
Medium

17993

759

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

Accepted
2,481,639
Submissions
5,642,901
''')
