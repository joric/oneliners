from lc import *

# https://leetcode.com/problems/remove-nodes-from-linked-list

class Solution:
    def removeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        if not h:
            return h
        v = eval(h.serialize(h))
        s = 0
        [v.pop(i)if s>v[i]else(s:=v[i])for i in range(len(v))[::-1]]
        return h.deserialize(str(v))

class Solution:
    def removeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return h and h.deserialize(str((v:=eval(h.serialize(h)),s:=0,[v.pop(i)if s>v[i]else(s:=v[i])for i in range(len(v))[::-1]],v)[3]))

class Solution:
    def removeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        v=eval(h.serialize(h));return h.deserialize(str([x for x,y in zip(v,[*accumulate(v[::-1],max)][::-1])if x>=y]))

# https://leetcode.com/problems/remove-nodes-from-linked-list/discuss/5119727/one-line-solution

class Solution:
    def removeNodes(self, n: Optional[ListNode]) -> Optional[ListNode]:
        if n.next:
            q = self.removeNodes(n.next)
            n.next = q
            if n.val < q.val:
                return q
        return n

class Solution:
    def removeNodes(self, n: Optional[ListNode]) -> Optional[ListNode]:
        return(f:=lambda n:n.next and(setattr(n,'next',q:=f(n.next)),q)[n.val<q.val]or n)(n)

class Solution:
    def removeNodes(s, n: Optional[ListNode]) -> Optional[ListNode]:
        return n.next and(setattr(n,'next',q:=s.removeNodes(n.next)),q)[n.val<q.val]or n

test('''
2487. Remove Nodes From Linked List
Medium

1388

36

Add to List

Share
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
Accepted
63,611
Submissions
96,611
''')