from lc import *

# collect values, python 3.12 because of batched()

class Solution:
    def swapPairs(s, h: Optional[ListNode]) -> Optional[ListNode]:
        n=(f:=lambda x:x and[x.val]+f(x.next)or[])(h);return n and ListNode(','.join(map(str,chain(*map(reversed,batched(sorted(n),2))))))or None

# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11095/Python-5-line-solution

class Solution:
    def swapPairs(self, h: Optional[ListNode]) -> Optional[ListNode]:
        d=p=ListNode(0);p.next=h
        while h and h.next:
            h.next.next,h.next,p.next,p,h=h,h.next.next,h.next,h,h.next.next
        return d.next

# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C%2B%2B-Python-Ruby

class Solution:
    def swapPairs(self, h: Optional[ListNode]) -> Optional[ListNode]:
        d = p = ListNode(0)
        p.next = h
        while p.next and p.next.next:
            a = p.next
            b = a.next
            p.next, a.next, b.next = b, b.next, a
            p = a
        return d.next

# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/1377185/4-line-of-code-only

class Solution:
    def swapPairs(self, h: Optional[ListNode]) -> Optional[ListNode]:
        if not h or not h.next:
            return h
        h.val,h.next.val=h.next.val,h.val
        self.swapPairs(h.next.next)
        return h

class Solution:
    def swapPairs(self, h):
        return (h and h.next and (t:=h.next.val,setattr(h.next,'val',h.val),setattr(h,'val',t)) and self.swapPairs(h.next.next),h)[1]

class Solution:
    def swapPairs(s, h: Optional[ListNode]) -> Optional[ListNode]:
        h and h.next and(t:=h.next.val,setattr(h.next,'val',h.val),setattr(h,'val',t),s.swapPairs(h.next.next));return h

class Solution:
    def swapPairs(s, h: Optional[ListNode]) -> Optional[ListNode]:
        h and h.next and(exec('h.val,h.next.val=h.next.val,h.val'),s.swapPairs(h.next.next));return h

test('''
24. Swap Nodes in Pairs
Medium

9636

365

Add to List

Share
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
Accepted
1,091,742
Submissions
1,774,366
Seen this question in a real interview before?

Yes

No
Reverse Nodes in k-Group
Hard
Swapping Nodes in a Linked List
Medium
''')

