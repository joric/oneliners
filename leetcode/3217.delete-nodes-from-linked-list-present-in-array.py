from lc import *

# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/discuss/5473536/One-Line-Solution

class Solution:
    def modifiedList(self, a: List[int], h: Optional[ListNode]) -> Optional[ListNode]:
        a={*a};return h.deserialize(str([x for x in eval(h.serialize(h))if x not in a]))

class Solution: # TLE
    def modifiedList(self, a: List[int], h: Optional[ListNode]) -> Optional[ListNode]:
        return h.deserialize(str([x for x in eval(h.serialize(h))if x not in a]))

class Solution:
    def modifiedList(self, a: List[int], h: Optional[ListNode]) -> Optional[ListNode]:
        return h.deserialize(str([*filterfalse({*a}.__contains__,eval(h.serialize(h)))]))

class Solution:
    def modifiedList(self, a: List[int], h: Optional[ListNode]) -> Optional[ListNode]:
        return(f:=lambda n,a={*a}:n and(ListNode(n.val,q:=f(n.next)),q)[n.val in a])(h)

class Solution:
    def modifiedList(self, a: List[int], h: Optional[ListNode]) -> Optional[ListNode]:
        return(f:=lambda n,a={*a}:n and(type(h)(n.val,q:=f(n.next)),q)[n.val in a])(h)

test('''
3217. Delete Nodes From Linked List Present in Array
Medium

125

4

Add to List

Share
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:



Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:



No node has value 5.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
The input is generated such that there is at least one node in the linked list that has a value not present in nums.
Accepted
42,384
Submissions
69,339
''')
