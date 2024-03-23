from lc import *

# https://leetcode.com/problems/reorder-list/discuss/514461/python-a-one-array-solution-with-explanation

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        n=len(a:=eval(h.serialize(h)))
        i = 0
        while h:
            h.val = a[~(i//2)]if i%2 else a[i//2]
            h = h.next
            i += 1

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        a=eval(h.serialize(h));next(0 for i in count()if setattr(h,'val',a[(i//2,~i//2)[i%2]])or not(h:=h.next))

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        a=eval(h.serialize(h));[setattr(h,'val',a[(i//2,~i//2)[i%2]])or(h:=h.next)for i in range(len(a))]

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        a=eval(h.serialize(h));h.next=h.deserialize(str([a[(i//2,~i//2)[i%2]]for i in range(1,len(a))]))

test('''
143. Reorder List
Medium

10343

369

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
Accepted
859,076
Submissions
1,522,865
''', check=lambda res,exp,h:str(h)==str(h.deserialize(str(exp)))
)
