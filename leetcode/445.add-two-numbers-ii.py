from lc import *

# https://leetcode.com/problems/add-two-numbers-ii/discuss/926807/Python-Two-stacks-solution-explained

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        carry, head = 0, None
        while st1 or st2 or carry:
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new
        return head

# https://leetcode.com/problems/add-two-numbers-ii/discuss/451705/7-lines-python

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        f=lambda n,p=0:n and f(n.next,p*10+n.val) or p
        l=lambda n,p=None:(x:=ListNode(n<9 and n or n%10,p))and n>9 and l(n//10,x)or x
        return l(f(l1)+f(l2))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return (l:=lambda n,p=None:(x:=ListNode(n<9 and n or n%10,p))and n>9 and l(n//10,x)or x)((i:=lambda n,p=0:n and i(n.next,p*10+n.val)or p)(l1)+i(l2))

# https://leetcode.com/problems/add-two-numbers-ii/discuss/927274/2-Liner-oror-Python-3-Solution-oror-beats-99.9

class Solution:
    def addTwoNumbers(self, a: ListNode, b: ListNode) -> ListNode:
        f=lambda n,p=0:n and f(n.next,p*10+n.val)or p;return ListNode(','.join([*str(f(a)+f(b))]))

test('''
445. Add Two Numbers II
Medium

4746

253

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?
''')
