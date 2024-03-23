from lc import *

# https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

# https://leetcode.com/problems/reorder-list/discuss/129896/One-Short-and-Humorous-Python-Solution

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        q, i = deque([]), 0
        while h:
            q.append(h)
            h = h.next
        while q:
            i = (i-1)%-2
            x = q.popleft() if i==-1 else q.pop()
            x.next = q[i] if q else None

# https://leetcode.com/problems/reorder-list/discuss/514461/python-a-one-array-solution-with-explanation

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        n=len(a:=eval(h.serialize(h)))
        i = 0
        while h:
            h.val = a[~(i//2)]if i%2 else a[i//2]
            h = h.next
            i += 1

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        t=type(h);a=t._list_node_to_array(h);h.next=t._array_to_list_node([a[(i//2,~i//2)[i%2]]for i in range(1,len(a))])

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        a=eval(h.serialize(h));h.next=h.deserialize(str([a[(i//2,~i//2)[i%2]]for i in range(1,len(a))]))

test('''
143. Reorder List
Medium

10343

369

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
Accepted
859,076
Submissions
1,522,865
''', check=lambda res,exp,h:str(h)==str(h.deserialize(str(exp)))
)
