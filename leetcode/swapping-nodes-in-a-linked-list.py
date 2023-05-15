from lc import *

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        a[k-1],a[-k] = a[-k],a[k-1]
        cur = dummy = ListNode()
        for x in a:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1033533/Ultra-Clean-Python-or-High-Speed

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = h
        for _ in range(k-1):
            n = n.next
        a = n
        b = h
        while n.next:
            b = b.next
            n = n.next
        a.val, b.val  =  b.val, a.val
        return h

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        return (n:=h,[(n:=n.next)for _ in range(k-1)],a:=n,b:=h,all(n.next and(b:=b.next,n:=n.next)for _ in count()),(t:=a.val,setattr(a,'val',b.val),setattr(b,'val',t)),h)[6]

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        return(n:=h,[(n:=n.next)for _ in range(k-1)],a:=n,b:=h,all(n.next and(b:=b.next,n:=n.next)for _ in count()),exec('a.val,b.val=b.val,a.val'),h)[6]

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        q = h
        i = 1
        d = {}
        while q:
            d[i] = q
            q = q.next
            i = i + 1
        d[k].val, d[i-k].val = d[i-k].val, d[k].val
        return h

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        return(q:=h,i:=1,d:={},all(q and(setitem(d,i,q),q:=q.next,i:=i+1)for _ in count()),exec('d[k].val,d[i-k].val=d[i-k].val,d[k].val'),h)[5]

class Solution:
    def swapNodes(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        q=h;i=1;d={};all(q and(setitem(d,i,q),q:=q.next,i:=i+1)for _ in count());d[k].val,d[i-k].val=d[i-k].val,d[k].val;return h

test('''
1721. Swapping Nodes in a Linked List
Medium

3905

130

Add to List

Share
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 10^0
Accepted
219,069
Submissions
325,159
Seen this question in a real interview before?

Yes

No
Remove Nth Node From End of List
Medium
Swap Nodes in Pairs
Medium
Reverse Nodes in k-Group
Hard
We can transform the linked list to an array this should ease things up
After transforming the linked list to an array it becomes as easy as swapping two integers in an array then rebuilding the linked list
''')

