from lc import *

# https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space

def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

# use recursion to reverse the list and compare values in a single pass

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        left = head
        def helper(node):
            nonlocal left
            if node.next and not helper(node.next):
                return False
            if left.val != node.val:
                return False
            left = left.next
            return True
        return helper(head)

# linked list expansion

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s==s[::-1]

class Solution:
    def isPalindrome(self, h: ListNode) -> bool:
        return(s:=type(h)._list_node_to_array(h))==s[::-1]

class Solution:
    def isPalindrome(self, h: ListNode) -> bool:
        s=type(h)._list_node_to_array(h);return s==s[::-1]

class Solution:
    def isPalindrome(self, h: ListNode) -> bool:
        s=eval(type(h).serialize(h));return s==s[::-1]

class Solution:
    def isPalindrome(self, h: ListNode) -> bool:
        return(s:=eval(type(h).serialize(h)))==s[::-1]

class Solution:
    def isPalindrome(self, h: ListNode) -> bool:
        return(s:=eval(h.serialize(h)))==s[::-1]

test('''
234. Palindrome Linked List
Easy

15933

861

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
Accepted
1,770,759
Submissions
3,402,437
''')
