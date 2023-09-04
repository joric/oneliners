from lc import *

def init(head: ListNode, pos: int):
    global p
    p = pos
    head.getTail().next = head.getNode(p)

def check(res,exp,head):
    i = head.getIndex(head.detectCycle())
    return p==i, 'no cycle' if i<0 else f'tail connects to node index {i}'

# from linked-list-cycle-ii (works)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return next(head for _ in count() if not head or head.val==inf or not(setattr(head,'val',inf),head:=head.next))

# floyd

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class Solution:
    def hasCycle(self, h: Optional[ListNode]) -> bool:
        s,f = h,h
        while f and f.next:
            s = s.next
            f = f.next.next
            if s==f:
                return True
        return False

class Solution:
    def hasCycle(self, h: Optional[ListNode]) -> bool:
        s,f,r = h,h,False
        while True:
            if not(f and f.next and (s:=s.next,f:=f.next.next) and not(r:=s==f)):
                return r
        return r

class Solution:
    def hasCycle(self, h: Optional[ListNode]) -> bool:
        print(h.detectCycle())
        s,f,r = h,h,0;return next(r for _ in count()if not(f and f.next and(s:=s.next,f:=f.next.next)and not(r:=s==f)))

test('''
141. Linked List Cycle
Easy

13756

1131

Add to List

Share
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Accepted
2,293,646
Submissions
4,735,707
''', init=init, check=check
)
