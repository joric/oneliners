from lc import *

# https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def reverse(head, count):
            prev, cur, nxt = None, head, head
            while count > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                count -= 1
            return (cur, prev) 

        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

class Solution:
    def reverseKGroup(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        batched=lambda a,n:(lambda i:iter(lambda:tuple(islice(i,n)),()))((i:=iter(a),)[0]);\
        return h.deserialize(str([*chain(*[x[::1-2*(len(x)>=k)]for x in batched(eval(h.serialize(h)),k)])]))

test('''
25. Reverse Nodes in k-Group
Hard

13846

716

Add to List

Share
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

Accepted
1,018,861
Submissions
1,691,599
''')
