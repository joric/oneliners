from lc import *

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        i = 0
        q = []
        for node in lists:
            if node:
                heappush(q, (node.val, i, node) )
                i += 1
        while q:
            curr.next = heappop(q)[2]
            curr = curr.next
            if curr.next:
                heappush(q, (curr.next.val, i, curr.next))
                i+=1
        return dummy.next

# https://leetcode.com/problems/merge-k-sorted-lists/discuss/279704/Python-4-lines-O(NlogN)-68ms-beat-97.27

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        r, n, p = [], lists and lists.pop(), None
        while lists or n:
            r[len(r):], n = ([n], n.next or lists and lists.pop()) if n else ([], lists.pop())
        for n in sorted(r, key=lambda x: x.val, reverse=True):
            n.next, p = p, n
        return n if r else None

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return (g:=lambda x:ListNode(x[0],g(x[1:]))if x else None)(sorted(itertools.chain(*[(f:=lambda x:x and [x.val]+f(x.next)or[])(h) for h in lists])))

test('''

23. Merge k Sorted Lists
Hard

15706

586

Add to List

Share
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.

Accepted
1,542,246
Submissions
3,144,945

''')

