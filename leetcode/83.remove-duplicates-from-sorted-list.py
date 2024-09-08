from lc import *

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28621/Simple-iterative-Python-6-lines-60-ms

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head

class Solution:
    def deleteDuplicates(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=ListNode;return t.deserialize(str(sorted([*{*eval(t.serialize(h))}])))

test('''
83. Remove Duplicates from Sorted List
Easy

8774

311

Add to List

Share
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
Accepted
1,644,113
Submissions
3,083,401
''')
