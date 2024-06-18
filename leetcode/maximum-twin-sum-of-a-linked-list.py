from lc import *

# bidirectional recursion

class Solution:
    def pairSum(self, h: Optional[ListNode]) -> int:
        a = h
        s = 0
        def f(b):
            nonlocal a, s
            return not b or f(b.next) and (s:=max(s,a.val+b.val),a:=a.next)[0]
        return f(h)

# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/discuss/1675645/JavaPython-3-One-pass-5-liner-O(n)-codes-w-brief-analysis.

class Solution:
    def pairSum(self, h: Optional[ListNode]) -> int:
        r = []
        while h:
            r.append(h.val)
            h = h.next
        return max(r[i]+r[~i] for i in range(len(r)//2))

class Solution:
    def pairSum(self, h: Optional[ListNode]) -> int:
        r=[(h.val,h:=h.next)[0]for _ in[1]*10**5 if h];return max(map(sum,zip(r,r[::-1])))

class Solution:
    def pairSum(self, h: Optional[ListNode]) -> int:
        return max(map(sum,zip(r:=[(h.val,h:=h.next)[0]for _ in[1]*10**5 if h],r[::-1])))

test('''
2130. Maximum Twin Sum of a Linked List
Medium

1696

43

Add to List

Share
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
Accepted
94,067
Submissions
116,914
Seen this question in a real interview before?

Yes

No
Reverse Linked List
Easy
Palindrome Linked List
Easy
Middle of the Linked List
Easy
How can "reversing" a part of the linked list help find the answer?
We know that the nodes of the first half are twins of nodes in the second half, so try dividing the linked list in half and reverse the second half.
How can two pointers be used to find every twin sum optimally?
Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums.
''')

