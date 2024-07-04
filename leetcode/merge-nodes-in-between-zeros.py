from lc import *

# https://leetcode.com/problems/merge-nodes-in-between-zeros/discuss/1784766/JavaPython-3-One-pass-two-pointers-copy-sum-to-0-nodes.

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-math.inf)
        while head and head.next:
            prev.next = head
            head = head.next
            while head and head.val != 0:
                prev.next.val += head.val
                head = head.next
            prev = prev.next
        prev.next = None    
        return dummy.next

class Solution:
    def mergeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        a = eval(h.serialize(h))
        r = []
        for x in a:
            x==0 and r.append(0)
            r[-1] += x
        r.pop()
        return h.deserialize(str(r))

class Solution:
    def mergeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h.deserialize(str([sum(v)for k,v in groupby(eval(h.serialize(h)),key=0..__lt__)if k]))

class Solution:
    def mergeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h._array_to_list_node(sum(v)for k,v in groupby(h._list_node_to_array(),truth)if k)

class Solution:
    def mergeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h.deserialize(str([sum(v)for k,v in groupby(eval(h.serialize(h)),truth)if k]))


test('''
2181. Merge Nodes in Between Zeros
Medium

1717

35

Add to List

Share
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

 

Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
Example 2:


Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
 

Constraints:

The number of nodes in the list is in the range [3, 2 * 105].
0 <= Node.val <= 1000
There are no two consecutive nodes with Node.val == 0.
The beginning and end of the linked list have Node.val == 0.
Accepted
117,860
Submissions
137,270
''')
