from lc import *

# heap-based

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        d = c = ListNode()
        h = []
        for i,e in enumerate(lists):
            if e:
                heappush(h,(e.val,i))
        while h:
            x,i = heappop(h)
            c.next = ListNode(x)
            c = c.next
            if lists[i].next:
                lists[i] = lists[i].next
                heappush(h,(lists[i].val,i))
        return d.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return next((d.next for _ in count() if not(h and (c:=(f:=lambda x,i,c:(setattr(c,'next',ListNode(x)),c:=c.next,
            lists[i].next and (setitem(lists,i,lists[i].next),heappush(h,(lists[i].val,i))),c)[-1])(*heappop(h),c)))),
            (h:=[],d:=(c:=ListNode()),[heappush(h,(e.val,i)) for i,e in enumerate(lists) if e]))

# list expansion

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return (g:=lambda x:ListNode(x[0],g(x[1:]))if x else None)(sorted(itertools.chain(*[(f:=lambda x:x and [x.val]+f(x.next)or[])(h) for h in lists])))

# updated 2024-02-13

class Solution:
    def mergeKLists(self, v: List[Optional[ListNode]]) -> Optional[ListNode]:
        return(g:=lambda x:x and ListNode(x[0],g(x[1:]))or None)(sorted(chain(*[(f:=lambda x:x and[x.val]+f(x.next)or[])(h)for h in v])))

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

