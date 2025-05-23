from lc import *

class Solution:
    def partition(self, h: ListNode, x: int) -> ListNode:
        p,q=a,b=ListNode(),ListNode()
        while h:
            if h.val < x:
                a.next = h
                a = a.next
            else:
                b.next = h
                b = b.next
            h = h.next
        b.next = None
        a.next = q.next
        return p.next

class Solution:
    def partition(self, h: ListNode, x: int) -> ListNode:
        def f(o,a,b,x):
            if o:
                if o.val < x:
                    a.next = o
                    a = a.next
                    b.next = None
                else:
                    b.next = o
                    b = b.next
                a = f(o.next,a,b,x)
            return a
        a, b = ListNode(), ListNode()
        q = f(h,a,b,x)
        q.next = b.next
        return a.next

class Solution:
    def partition(self, h: Optional[ListNode], x: int) -> Optional[ListNode]:
        t=a,b=[ListNode(),ListNode()]
        while h:
            t[h.val>=x].next,t[h.val>=x],h=h,h,h.next
        t[1].next = None
        t[0].next = b.next
        return a.next

class Solution:
    def partition(self, h: ListNode, x: int) -> ListNode:
        f=lambda x:x and[x.val]+f(x.next)or[];return ListNode(','.join(map(str,[i for i in f(h)if i<x]+[i for i in f(h)if i>=x])))

class Solution:
    def partition(self, h: ListNode, x: int) -> ListNode:
        f=lambda x:x and[x.val]+f(x.next)or[];c=[],[];[c[i<x].append(str(i))for i in f(h)];return ListNode(','.join(c[1]+c[0]))

class Solution:
    def partition(self, h: ListNode, x: int) -> ListNode:
        c=[],[];(f:=lambda r:r and(c[r.val<x].append(str(r.val)),f(r.next)))(h);return ListNode(','.join(c[1]+c[0]))

class Solution:
    def partition(self, h: ListNode, x: int) -> ListNode:
        f=lambda r,o:r and([],[str(r.val)])[o(r.val,x)]+f(r.next,o)or[];return ListNode(','.join(f(h,lt)+f(h,ge)))

test('''
86. Partition List
Medium

5756

658

Add to List

Share
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
''')