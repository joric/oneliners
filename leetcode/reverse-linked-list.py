from lc import *

# linked list expansion

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = h
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        p=None;c=h;return next((p for _ in count()if not(c and(n:=c.next,setattr(c,'next',p),p:=c,c:=n))),p)

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=type(h);return h and t(','.join(map(str,t._list_node_to_array(h)[::-1])))

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=type(h);return h and t(','.join(map(str,eval(t.serialize(h))[::-1])))

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=type(h);return h and t.deserialize(str(eval(t.serialize(h))[::-1]))

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h and(t:=type(h)).deserialize(str(eval(t.serialize(h))[::-1]))

# https://leetcode.com/problems/reverse-linked-list/discuss/4905803/one-line-solution

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        while h:
            h.next,h,p = p,h.next,h
        return p

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return exec('while h:h.next,h,p=p,h.next,h',g:={'p':None,'h':h})or g['p']

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        exec('while h:h.next,h,p=p,h.next,h',g:={'p':None,'h':h});return g['p']

# even shorter

class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h and h.deserialize(str(eval(h.serialize(h))[::-1]))

#class Solution:
#    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
#        print(h)

test('''
206. Reverse Linked List
Easy

20805

410

Add to List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Accepted
3,881,989
Submissions
5,113,473
''')
