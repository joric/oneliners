from lc import *

def init(head: ListNode, pos: int):
    global p
    p = pos
    head.getTail().next = head.getNode(p)

def check(res,exp,head):
    global p
    i = head.getIndex(head.detectCycle())
    return p==i, ('no cycle' if i<0 else f'tail connects to node index {i}')

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow 

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        while head:
            if head.val==inf:
                return head
            head.val = inf
            head = head.next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return next(head for _ in count() if not head or head.val==inf or not(setattr(head,'val',inf),head:=head.next))

test('''

142. Linked List Cycle II
Medium

10385

766

Add to List

Share
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Accepted
955,481
Submissions
2,012,559
''', init=init, check=check,
)

