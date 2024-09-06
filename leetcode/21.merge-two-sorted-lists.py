from lc import *

# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python

class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a

class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        a,b=map(eval,map(ListNode.serialize,(a,b)));return ListNode.deserialize(str(sorted(a+b)))

test('''
21. Merge Two Sorted Lists
Easy

22017

2152

Add to List

Share
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
Accepted
4,491,318
Submissions
6,892,824
''')
