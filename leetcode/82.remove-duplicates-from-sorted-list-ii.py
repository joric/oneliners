from lc import *

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28336/Python-in-place-solution-with-dummy-head-node.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

class Solution:
    def deleteDuplicates(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=ListNode;return t.deserialize(str([k for k,v in Counter(eval(t.serialize(h))).items()if v==1]))

class Solution:
    def deleteDuplicates(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=ListNode;p=eval(t.serialize(h));return t.deserialize(str([x for x in p if p.count(x)<2]))

test('''
82. Remove Duplicates from Sorted List II
Medium

8884

246

Add to List

Share
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]

Other examples:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
Accepted
789,313
Submissions
1,636,957
''')
