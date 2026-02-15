from lc import *

# https://leetcode.com/problems/sort-list/solutions/5099670/only-four-lines-solution-by-charnavoki-f7vr/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort(reverse=True)
        head = None
        for val in arr:
            head = ListNode(val, head)
        return head

class Solution:
    def sortList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=ListNode;return t._array_to_list_node(sorted(t._list_node_to_array(h)))

class Solution:
    def sortList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        t=ListNode;return t.deserialize(str(sorted(eval(t.serialize(h)))))

test('''
148. Sort List
Solved
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,223,751/1.9M
Acceptance Rate
63.8%
Topics
Linked List
Two Pointers
Divide and Conquer
Sorting
Merge Sort
icon
Companies
Similar Questions
Merge Two Sorted Lists
Easy
Sort Colors
Medium
Insertion Sort List
Medium
Sort Linked List Already Sorted Using Absolute Values
Medium
''')
