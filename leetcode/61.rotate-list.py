from lc import *

# https://leetcode.com/problems/rotate-list/discuss/883252/Python-O(n)-solution-explained

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        last, n = head, 1
        while last.next:
            last = last.next
            n += 1
        if k % n == 0: return head
        middle = head
        for i in range(n - k%n-1):
            middle = middle.next
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head

class Solution:
    def rotateRight(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        t=ListNode;p=(q:=deque(eval(t.serialize(h)))).rotate(k)or q;return t.deserialize(str([*p]))

test('''
61. Rotate List
Medium

9810

1461

Add to List

Share
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Other examples:

Input: head = [], k = 0
Output: []

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
Accepted
1,061,045
Submissions
2,751,789
''')
