from lc import *

# https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python

class Solution:
    def summaryRanges(self, n: List[int]) -> List[str]:
        o=r=[];[(x-1not in r and(r:=[],o:=o+[r]),setitem(r,slice(1,None),[x]))for x in n];return['->'.join(map(str,r))for r in o]

test('''
228. Summary Ranges
Easy

2687

1440

Add to List

Share
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
Accepted
355,111
Submissions
748,409
Seen this question in a real interview before?

Yes

No
Missing Ranges
Easy
Data Stream as Disjoint Intervals
Hard
Find Maximal Uncovered Ranges
Medium
''')

