from lc import *

# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0    
        root = p = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1, l1 = l1.val, l1.next
            if l2:
                v2, l2 = l2.val, l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            p.next = ListNode(val)
            p = p.next
        return root.next

class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        f = lambda n:n and n.val+10*f(n.next) or 0
        l = lambda n: ListNode(n%10, l(n//10) if n>9 else None)
        return l(f(a)+f(b))

# ListNode(bool) does not work anymore
class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        return(g:=lambda n:ListNode(n%10,n>9 and g(n//10)))((f:=lambda n:n and n.val+10*f(n.next)or 0)(a)+f(b))

class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        f,g=lambda n:n and n.val+10*f(n.next)or 0,lambda n:ListNode(n%10,n>9and g(n//10)or None);return g(f(a)+f(b))

# serialize-based

# ListNode('x,y,...') does not work anymore
class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        f=lambda n:n and n.val+10*f(n.next)or 0;return ListNode(','.join([*str(f(a)+f(b))][::-1]))

class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        f=lambda n:n and n.val+10*f(n.next)or 0;return a.deserialize(str([int(c)for c in str(f(a)+f(b))[::-1]]))

class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        f=lambda n:n and n.val+10*f(n.next)or 0;return a.deserialize(str([*starmap(int,str(f(a)+f(b))[::-1])]))

test('''
2. Add Two Numbers

Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
''')