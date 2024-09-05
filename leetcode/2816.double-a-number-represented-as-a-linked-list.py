from lc import *

# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/discuss/3901745/Python-3-oror-5-lines-in-place-recursion-oror-TM%3A-330-ms-30-MB

class Solution:
    def doubleIt(self, h: Optional[ListNode]) -> Optional[ListNode]:
        def f(h):
            x = 2*h.val + (f(h.next) if h.next else 0)
            h.val = x%10
            return x//10
        return ListNode(1,h)if f(h) else h

class Solution:
    def doubleIt(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return type(h)(1,h)if(f:=lambda h:setattr(h,'val',(x:=2*h.val+(f(h.next)if h.next else 0))%10)or x//10)(h)else h

# convert list
class Solution:
    def doubleIt(self, h: Optional[ListNode]) -> Optional[ListNode]:
        f=lambda n,p=0:n and f(n.next,p*10+n.val)or p
        l=lambda n,p=None:(x:=ListNode(n<9 and n or n%10,p))and n>9 and l(n//10,x)or x
        return l(2*f(h))

# serialize
class Solution:
    def doubleIt(self, h: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(0);return type(h)(','.join(str(2*int(''.join(map(str,eval(h.serialize(h))))))))

class Solution:
    def doubleIt(self, h: Optional[ListNode]) -> Optional[ListNode]:
        set_int_max_str_digits(0);return type(h)(','.join(str(2*int(re.sub('[^0-9]','',h.serialize(h))))))

test('''
2816. Double a Number Represented as a Linked List
Medium

489

8

Add to List

Share
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:


Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
Accepted
42,764
Submissions
85,754
''')