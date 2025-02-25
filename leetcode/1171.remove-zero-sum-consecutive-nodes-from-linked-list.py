from lc import *

# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap

class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        p = c = ListNode(0)
        p.next = h
        s,d = 0,{}
        while c:
            s += c.val
            t = d.get(s,c)
            while s in d:
                d.popitem()
            d[s] = t
            t.next = c = c.next
        return p.next

class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        d[0] = p = ListNode(0)
        p.next = h
        s = 0
        while h:
            s += h.val
            d[s] = h
            h = h.next
        h = p
        s = 0
        while h:
            s += h.val
            h.next = d[s].next
            h = h.next
        return p.next

# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/4863159/Use-bruteforce-in-the-Array-No-prefix-sum-!!

class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        a=(f:=lambda x:x and[x.val]+f(x.next)or[])(h)
        n = len(a)
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += a[j]
                if s==0:
                    a[i:j+1]=[0]*(j+1-i)
                    break
        return ListNode(str([*filter(None,a)])[1:-1])

# linked list expansion

class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        a=(f:=lambda x:x and[x.val]+f(x.next)or[])(h);n=len(a);[(s:=0,any(0==(s:=s+a[j])and[setitem(a,slice(i,j+1),[0]*(j+1-i))] for j in range(i,n)))for i in range(n)];return ListNode(str([*filter(None,a)])[1:-1])

# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/4735031/JAVA-simple-recursive-function

class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        if h:
            h.next = self.removeZeroSumSublists(h.next)
            s,c = 0,h
            while c:
                s += c.val
                if s==0:
                    return c.next
                c = c.next
            return h

class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return(f:=lambda h:h and setattr(h,'next',f(h.next))or(g:=lambda s,c:(g(s,c.next)if(s:=s+c.val)else c.next)if c else h)(0,h))(h)

test('''
1171. Remove Zero Sum Consecutive Nodes from Linked List
Medium

2176

98

Add to List

Share
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [[3,1],[1,2,1]]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
Accepted
53,303
Submissions
122,569
''',check=lambda res,exp,*args:any(str(res)==str(t) for t in d) if len(d:=ListNode.dump(exp))>1 and type(d[0]) is list else str(res)==str(exp)
)