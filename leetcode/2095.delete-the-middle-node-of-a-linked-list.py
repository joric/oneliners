from lc import *

# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/822021085/?envType=daily-question&envId=2026-06-15

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next, slow, fast, prev = head, head, head, dummy
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return dummy.next

class Solution:
    def deleteMiddle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        d.next,s,f,p =h,h,h,d
        while f and f.next:
            p=s
            s=s.next
            f=f.next.next
        p.next = s.next
        return d.next

class Solution:
    def deleteMiddle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode();d.next,s,f,p =h,h,h,d;all(f and f.next and(p:=s,s:=s.next,f:=f.next.next)for _ in count());p.next=s.next;return d.next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def f(a, b):
            if not b:
                return a.next
            a.next = f(a.next, b.next.next) if b.next else f(a.next, b.next)
            return a
        return f(head, head.next)

class Solution:
    def deleteMiddle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return(f:=lambda a,b:setattr(a,'next',f(a.next,b.next.next)if b.next else f(a.next,b.next))or a if b else a.next)(h,h.next)

# POTD 2026-06-14

class Solution:
    def deleteMiddle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        a=eval(h.serialize(h));n=len(a)//2;return h.deserialize(str(a[:n]+a[n+1:]))

class Solution:
    def deleteMiddle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        a=eval(h.serialize(h));a.pop(len(a)//2);return h.deserialize(str(a))

test('''
2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105

''')