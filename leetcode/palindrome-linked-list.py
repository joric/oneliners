from lc import *

# https://leetcode.com/problems/palindrome-linked-list/

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
