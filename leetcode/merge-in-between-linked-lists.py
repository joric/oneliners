from lc import *

# https://leetcode.com/problems/merge-in-between-linked-lists/discuss/952030/JavaPython-3-Straight-forward-codes-w-comments-and-analysis.

class Solution:
    def mergeInBetween(self, p: ListNode, a: int, b: int, q: ListNode) -> ListNode:
        s, e = None, p
        for i in range(b):
            if i == a - 1:
                s = e
            e = e.next
        s.next = q
        while q.next:
            q = q.next
        q.next = e.next
        e.next = None
        return p

# linked list expansion

class Solution:
    def mergeInBetween(self, p: ListNode, a: int, b: int, q: ListNode) -> ListNode:
        f=lambda x:x and[x.val]+f(x.next)or[];p=f(p);return ListNode(','.join(map(str,p[:a]+f(q)+p[b+1:])))

class Solution:
    def mergeInBetween(self, p: ListNode, a: int, b: int, q: ListNode) -> ListNode:
        f=type(p)._list_node_to_array;p=f(p);return ListNode(','.join(map(str,p[:a]+f(q)+p[b+1:])))

class Solution:
    def mergeInBetween(self, p: ListNode, a: int, b: int, q: ListNode) -> ListNode:
        f=type(p)._list_node_to_array;p=f(p);p[a:b+1]=f(q);return ListNode(','.join(map(str,p)))

class Solution:
    def mergeInBetween(self, p: ListNode, a: int, b: int, q: ListNode) -> ListNode:
        l=type(p);f=l._list_node_to_array;p=f(p);p[a:b+1]=f(q);return l(','.join(map(str,p)))

test('''
1669. Merge In Between Linked Lists
Medium

1564

191

Add to List

Share
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

 

Example 1:


Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
 

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
Accepted
99,127
Submissions
133,616
''')
