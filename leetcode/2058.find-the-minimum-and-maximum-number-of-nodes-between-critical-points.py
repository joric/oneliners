from lc import *

# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/discuss/2719832/Python-3-oror-11-lines-w-explanation-oror-TS%3A-82-88

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        ct, p, prev = 0, [], head.val
        while head.next:
            if (prev-head.val)*(head.val-head.next.val) < 0:
                p.append(ct)
            prev, head = head.val, head.next
            ct += 1
        n = len(p)
        if n < 2: return [-1,-1]
        mn = min((p[i]-p[i-1] for i in range(1,n)))
        mx = p[-1] - p[0]
        return [mn, mx]

# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/discuss/3483921/Python3-convert-to-list

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
        n=len(l)
        critical=[]
        for i in range(1,n-1):
            if l[i]>l[i-1] and l[i]>l[i+1] or l[i]<l[i-1] and l[i]<l[i+1]:
                critical.append(i)
        n=len(critical)
        if n<=1:
            return [-1,-1]
        mn=min(critical[i+1]-critical[i] for i in range(n-1))
        mx=critical[-1]-critical[0]
        return [mn,mx]

class Solution:
    def nodesBetweenCriticalPoints(self, h: Optional[ListNode]) -> List[int]:
        r=eval(h.serialize(h));p=[i for i in range(1,len(r)-1)if r[i]>r[i-1]and r[i]>r[i+1]or r[i]<r[i-1]and r[i]<r[i+1]];return p[1:]and(min(p[i+1]-p[i]for i in range(len(p)-1)),p[-1]-p[0])or[-1]*2

class Solution:
    def nodesBetweenCriticalPoints(self, h: Optional[ListNode]) -> List[int]:
        r=eval(h.serialize(h));p=[i for i in range(1,len(r)-1)if not min(r[i-1],r[i+1])<=r[i]<=max(r[i-1],r[i+1])];return p[1:]and(min(map(sub,p[1:],p)),p[-1]-p[0])or[-1]*2

class Solution:
    def nodesBetweenCriticalPoints(self, h: Optional[ListNode]) -> List[int]:
        r=eval(h.serialize(h));p=[i for i,(a,x,b)in enumerate(zip(r,r[1:],r[2:]))if not min(a,b)<=x<=max(a,b)];return p[1:]and(min(map(sub,p[1:],p)),p[-1]-p[0])or[-1]*2

class Solution:
    def nodesBetweenCriticalPoints(self, h: Optional[ListNode]) -> List[int]:
        r=eval(h.serialize(h));p=[i for i,(a,x,b)in enumerate(zip(r,r[1:],r[2:]))if(min(a,b)<=x<=max(a,b))-1];return p[1:]and(min(map(sub,p[1:],p)),p[-1]-p[0])or[-1]*2

test('''
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Medium

676

27

Add to List

Share
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

 

Example 1:


Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].
Example 2:


Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
Example 3:


Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.
 

Constraints:

The number of nodes in the list is in the range [2, 105].
1 <= Node.val <= 105
Accepted
37,030
Submissions
63,145
''')