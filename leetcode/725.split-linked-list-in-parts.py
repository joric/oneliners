from lc import *

# https://leetcode.com/problems/split-linked-list-in-parts/discuss/186563/Python-8-lines-O(n)-time-O(1)-extra-space-with-explanation

class Solution:
    def splitListToParts(self, r: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        p,n = r,0
        while p:
            p,n = p.next,n+1
        i,p,(q,r),s = 0,r,divmod(n,k),[None]*k
        while i<k and p:
            s[i] = p
            for _ in range(q-(i>=r)):
                p = p.next
            p.next,p,i = None,p.next,i+1
        return s

class Solution:
    def splitListToParts(self, r: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        p=r;n=sum(0!=(p:=p.next)for _ in[1]*10**5 if p);i,p,(q,r),s=0,r,divmod(n,k),[None]*k;return next(s for _ in count()if not(i<k and p and (setitem(s,i,p),[(p:=p.next)for _ in range(q-(i>=r))],t:=p.next,setattr(p,'next',None),p:=t,i:=i+1)))

class Solution:
    def splitListToParts(self, r: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        c=[(r.val,r:=r.next)[0]for _ in[0]*1000 if r];j,(d,r)=0,divmod(len(c),k);c=[c[j:(j:=j+d-(i>=r)+1)]for i in range(k)];return[v and ListNode(','.join(map(str,v)))or None for v in c]

class Solution:
    def splitListToParts(self, r: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        c=[(str(r.val),r:=r.next)[0]for _ in[0]*1000 if r];j,(d,r)=0,divmod(len(c),k);c=[c[j:(j:=j+d-(i>=r)+1)]for i in range(k)];return[v and ListNode(','.join(v))or None for v in c]

# updated 2024-09-06

class Solution:
    def splitListToParts(self, r: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        t=ListNode;c=eval(t.serialize(r));j,(d,x)=0,divmod(len(c),k);e=[c[j:(j:=j+d-(i>=x)+1)]for i in range(k)];return[t.deserialize(str(v))for v in e]

test('''
725. Split Linked List in Parts
Medium

2572

242

Add to List

Share
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


Other examples:

Input: head = [], k = 3
Output: [[],[],[]]

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
''')
