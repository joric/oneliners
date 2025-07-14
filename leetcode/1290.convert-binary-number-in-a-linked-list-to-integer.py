from lc import *

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solutions/1615736/simple-5-line-solution-python-time-o-n-space-o-1/?envType=daily-question&envId=2025-07-14

class Solution:
    def getDecimalValue(self, h: ListNode) -> int:
        r = 0
        while h:
            r = r*2+h.val
            h = h.next
        return r

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solutions/6932144/one-line-solution/?envType=daily-question&envId=2025-07-14

class Solution:
    def getDecimalValue(self, head: Optional[ListNode], res: int = 0) -> int:
        return  res if not head else self.getDecimalValue(head.next, res << 1 | head.val)

class Solution:
    def getDecimalValue(self, h: Optional[ListNode]) -> int:
        return int((f:=lambda h:h and str(h.val)+f(h.next)or'')(h),2)

class Solution:
    def getDecimalValue(self, h: Optional[ListNode]) -> int:
        return(f:=lambda h,r:h and f(h.next,r<<1|h.val)or r)(h,0)

class Solution:
    def getDecimalValue(self, h: Optional[ListNode]) -> int:
        return int(''.join(map(str,eval(h.serialize(h)))),2)

test('''
1290. Convert Binary Number in a Linked List to Integer
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0


Other examples:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
554,301/682.4K
Acceptance Rate
81.2%
Topics
Linked List
Math
icon
Companies
Hint 1
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.
Hint 2
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.
''')
